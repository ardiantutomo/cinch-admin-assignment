from pydantic import BaseModel
from datetime import datetime


class Attribute(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
