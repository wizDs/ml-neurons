import logging
import base64
import os
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
from processes import ProcessA, ProcessB, ProcessC
from request_body import (
    InputImage,
    InputSummary,
    InputWorkflow
)
from schemas import (
    SchemaProcessA1,
    SchemaProcessA2,
    SchemaProcessB,
    SchemaProcessC,
    SchemaWorkflow
)

API_ENCODING = "ISO-8859-1"

app = FastAPI()
logging.basicConfig(level=logging.INFO)

# import process prompts
MODEL = os.environ.get(key="MODEL", default="gpt-4o")
logging.info(f"{MODEL=}")
llm = ChatOpenAI(model=MODEL,
                 api_key=os.environ["OPENAI_API_KEY"])
process_a = ProcessA(llm=llm)
process_b = ProcessB(llm=llm)
process_c = ProcessC(llm=llm)


@app.post("/process-a1/", response_model=list[SchemaProcessA1])
async def describe_key_elements_of_advert(body: InputImage) -> list[SchemaProcessA1]:
    base64_encoded_image = base64.b64encode(body.image.encode(API_ENCODING)).decode("utf-8")
    output: list[dict] = process_a.run_a1(base64_encoded_image)
    return list(map(SchemaProcessA1.model_validate, output))


@app.post("/process-a2/", response_model=list[SchemaProcessA2])
async def describe_most_visually_salient_elements(body: InputImage) -> list[SchemaProcessA2]:
    base64_encoded_image = base64.b64encode(body.image.encode(API_ENCODING)).decode("utf-8")
    output: list[dict] = process_a.run_a2(base64_encoded_image)
    return list(map(SchemaProcessA2.model_validate, output))


@app.post("/process-b/", response_model=list[SchemaProcessB])
async def assess_cognitive_load(body: InputImage) -> list[SchemaProcessB]:
    base64_encoded_image = base64.b64encode(body.image.encode(API_ENCODING)).decode("utf-8")
    output: list[dict] = process_b.run(base64_encoded_image)
    return list(map(SchemaProcessB.model_validate, output))


@app.post("/process-c/", response_model=list[SchemaProcessC])
async def summarise_outputs(body: InputSummary) -> list[SchemaProcessC]:
    output: list[dict] = process_c.run(body.first_output, body.second_output)
    return list(map(SchemaProcessC.model_validate, output))


@app.post("/workflow/", response_model=SchemaWorkflow)
async def summarise_outputs(body: InputWorkflow) -> SchemaWorkflow:
    base64_encoded_image = base64.b64encode(body.image.encode(API_ENCODING)).decode("utf-8")
    base64_encoded_heatmap = base64.b64encode(body.heatmap.encode(API_ENCODING)).decode("utf-8")

    output_a: list[dict] = process_a.run(base64_encoded_image, base64_encoded_heatmap)
    output_b: list[dict] = process_b.run(base64_encoded_image)
    output_c: list[dict] = process_c.run(output_a, output_b)

    output = next(map(SchemaProcessC.model_validate, output_c))
    prev_processes = None if not body.all else output_a+output_b
    return SchemaWorkflow(summary=output, 
                          prev_processes=prev_processes)