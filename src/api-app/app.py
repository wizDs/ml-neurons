import os
from typing import Optional
from fastapi import FastAPI
from langchain_openai import ChatOpenAI
import pydantic
from dotenv import load_dotenv
from processes import ProcessA, ProcessB, ProcessC
import image_utils

load_dotenv()


class Image(pydantic.BaseModel):
    base64_encoded_image: str

class SchemaProcessA1(pydantic.BaseModel):
    ad_description: str
    ad_purpose: str


class SchemaProcessA2(pydantic.BaseModel):
    saliency_description: str


class SchemaProcessB(pydantic.BaseModel):
    cognitive_description: str


class SchemaProcessC(pydantic.BaseModel):
    ad_description: str
    ad_purpose: str
    saliency_description: str
    cognitive_description: str

class SchemaWorkflow(pydantic.BaseModel):
    prev_processes: Optional[list[dict]]
    summary: SchemaProcessC

app = FastAPI()

# import process prompts
llm = ChatOpenAI(model="gpt-4o-mini", api_key=os.environ["OPENAI_API_KEY"])
process_a = ProcessA(llm=llm)
process_b = ProcessB(llm=llm)
process_c = ProcessC(llm=llm)

@app.post("/process-a1/", response_model=list[SchemaProcessA1])
async def describe_key_elements_of_advert(image_path: str) -> list[SchemaProcessA1]:
    base64_encoded_image = image_utils.image_to_base64(image_path)
    output: list[dict] = process_a.run_a1(base64_encoded_image)
    return list(map(SchemaProcessA1.model_validate, output))


@app.post("/process-a2/", response_model=list[SchemaProcessA2])
async def describe_most_visually_salient_elements(image_path: str) -> list[SchemaProcessA2]:
    base64_encoded_image = image_utils.image_to_base64(image_path)
    output: list[dict] = process_a.run_a2(base64_encoded_image)
    return list(map(SchemaProcessA2.model_validate, output))


@app.post("/process-b/", response_model=list[SchemaProcessB])
async def assess_cognitive_load(image_path: str) -> list[SchemaProcessB]:
    base64_encoded_image = image_utils.image_to_base64(image_path)
    output: list[dict] = process_b.run(base64_encoded_image)
    return list(map(SchemaProcessB.model_validate, output))


@app.post("/process-c/", response_model=list[SchemaProcessC])
async def summarise_outputs(first_output: str, second_output: str) -> list[SchemaProcessC]:
    output: list[dict] = process_c.run(first_output, second_output)
    return list(map(SchemaProcessC.model_validate, output))


@app.post("/workflow/", response_model=SchemaWorkflow)
async def summarise_outputs(image_path: str, heatmap_path: str, all: bool=False) -> SchemaWorkflow:
    base64_encoded_image = image_utils.image_to_base64(image_path)
    base64_encoded_heatmap = image_utils.image_to_base64(heatmap_path)

    output_a: list[dict] = process_a.run(base64_encoded_image, base64_encoded_heatmap)
    output_b: list[dict] = process_b.run(base64_encoded_image)
    output_c: list[dict] = process_c.run(output_a, output_b)

    output = next(map(SchemaProcessC.model_validate, output_c))
    prev_processes = None if not all else output_a+output_b
    return SchemaWorkflow(summary=output, 
                          prev_processes=prev_processes)