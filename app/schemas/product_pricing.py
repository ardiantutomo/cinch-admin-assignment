from pydantic import BaseModel
from datetime import datetime


class ProductPricing(BaseModel):
    rental_period_id: int
    region_id: int
    price: float
    created_at: datetime
    updated_at: datetime
