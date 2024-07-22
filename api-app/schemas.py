from typing import Optional
from pydantic import BaseModel

class SchemaProcessA1(BaseModel):
    ad_description: str
    ad_purpose: str


class SchemaProcessA2(BaseModel):
    saliency_description: str


class SchemaProcessB(BaseModel):
    cognitive_description: str


class SchemaProcessC(BaseModel):
    ad_description: str
    ad_purpose: str
    saliency_description: str
    cognitive_description: str

class SchemaWorkflow(BaseModel):
    prev_processes: Optional[list[dict]]
    summary: SchemaProcessC
