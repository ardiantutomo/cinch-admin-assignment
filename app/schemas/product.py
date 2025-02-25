from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from app.schemas.product_attribute import ProductAttribute


class Product(BaseModel):
    id: int
    name: str
    description: str
    sku: str
    created_at: datetime
    updated_at: datetime
