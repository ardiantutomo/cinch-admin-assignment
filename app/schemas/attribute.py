from pydantic import BaseModel
from datetime import datetime


class AttributeCreate(BaseModel):
    name: str


class Attribute(BaseModel):
    id
    name: str
    created_at: datetime
    updated_at: datetime
