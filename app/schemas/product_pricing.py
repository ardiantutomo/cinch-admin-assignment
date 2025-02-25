from pydantic import BaseModel
from datetime import datetime

class ProductPricing(BaseModel):
    id: int
    product_id: int
    rental_period_id: int
    region_id: int
    price: float
    created_at: datetime
    updated_at: datetime
