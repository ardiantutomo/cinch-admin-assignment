from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Region(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime
