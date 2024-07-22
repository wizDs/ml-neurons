from pydantic import BaseModel

class InputImage(BaseModel):
    """image as a byte-array and decoded as ISO-8859-1 """
    image: str

class InputSummary(BaseModel):
    """imputs two summaries"""
    first_output: str
    second_output: str

class InputWorkflow(BaseModel):
    """images as a byte-array and decoded as ISO-8859-1 """
    image: str
    heatmap: str
    all: bool = False
