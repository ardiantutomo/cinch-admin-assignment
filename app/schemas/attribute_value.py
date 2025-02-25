from pydantic import BaseModel
from datetime import datetime


class AttributeValue(BaseModel):
    id: int
    attribute_id: int
    value: str
    created_at: datetime
    updated_at: datetime
