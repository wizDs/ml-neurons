import json
from langchain_core.messages import SystemMessage
from langchain_core.prompts import ChatPromptTemplate
from prompts import NeuronPrompts
from image_utils import image_message, GenericMessage
from json.decoder import JSONDecodeError

neuron_prompts = NeuronPrompts()

def load_json(content: str):
    """error handling of json"""
    if content.startswith("```json\n") and content.endswith("```"):
        # remove first 8 chars
        content = content[8:] 
        # remove last 3 chars
        content = content[:-3] 
    try:
        return json.loads(content)
    except JSONDecodeError:
        raise ValueError(f"content is not json: {content=}")
    except Exception as e:
        raise Exception(e)
        


class ProcessA:
    def __init__(self, llm):
        
        self.llm = llm
        self.prompt_A1 = ChatPromptTemplate.from_messages([SystemMessage(neuron_prompts.A1),
                                                           image_message("image_data")])
        self.prompt_A2 = ChatPromptTemplate.from_messages([SystemMessage(neuron_prompts.A2),
                                                           image_message("heatmap_image_data")])
        
        self.chain1 = self.prompt_A1 | self.llm
        self.chain2 = self.prompt_A2 | self.llm
        
    def run(self, image_data: str, heatmap_image_data: str) -> list[dict]:
        response1 = self.run_a1(image_data)
        response2 = self.run_a2(heatmap_image_data)
        return response1 + response2

            
    def run_a1(self, image_data: str) -> list[dict]:
        try:
            content = self.chain1.invoke({"image_data": image_data}).content
        except Exception as e:
            raise Exception(e)
        
        return load_json(content)


    def run_a2(self, heatmap_image_data: str) -> list[dict]:
        try:
            content = self.chain2.invoke({"heatmap_image_data": heatmap_image_data}).content
        except Exception as e:
            raise Exception(e)
        
        return load_json(content)

        

    def __repr__(self) -> None:
        return f"Prompt 1:\n\n{neuron_prompts.A1}\n\nPrompt 2:\n\n{neuron_prompts.A2}"


class ProcessB:
    def __init__(self, llm):
        
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages([SystemMessage(neuron_prompts.B),
                                                        image_message("image_data")])
        
        self.chain = self.prompt | self.llm
        
    def run(self, image_data: str) -> list[dict]:
        try:
            content = self.chain.invoke({"image_data": image_data}).content
        except Exception as e:
            raise Exception(e)
        
        return load_json(content)

    
    
    def __repr__(self) -> None:
        return f"Prompt:\n\n{neuron_prompts.B}"


class ProcessC:
    def __init__(self, llm):
        
        self.llm = llm
        self.prompt = ChatPromptTemplate.from_messages(
            [SystemMessage(neuron_prompts.C), 
             GenericMessage(role='user',
                            content="The first output is here: {first_output} \n\nand the second output is here:{second_output}")]
        )
        
        self.chain = self.prompt | self.llm
        
    def run(self, first_output: str, second_output: str) -> list[dict]:
        try:
            content = self.chain.invoke({"first_output": first_output,
                                         "second_output": second_output}).content
        except Exception as e:
            raise Exception(e)
        
        return load_json(content)

    def __repr__(self) -> None:
        return f"Prompt:\n\n{neuron_prompts.C}"
