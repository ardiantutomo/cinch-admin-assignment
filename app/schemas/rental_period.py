from pydantic import BaseModel
from datetime import datetime


class RentalPeriodCreate(BaseModel):
    months: int


class RentalPeriod(BaseModel):
    id: int
    months: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
