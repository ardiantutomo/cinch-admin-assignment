from pydantic import BaseModel
from datetime import datetime


class RentalPeriod(BaseModel):
    id: int
    months: int
    created_at: datetime
    updated_at: datetime
