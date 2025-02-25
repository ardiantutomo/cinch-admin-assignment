from pydantic import BaseModel
from typing import List
from typing import Optional


class ProductPricingCreate(BaseModel):
    rental_period_id: int
    region_id: int
    price: float


class ProductAttributeCreate(BaseModel):
    attribute_value_id: Optional[int] = None
    attribute_id: int
    value: str


class ProductCreate(BaseModel):
    name: str
    description: str
    sku: str
    pricings: List[ProductPricingCreate]
    attributes: List[ProductAttributeCreate]


class Product(BaseModel):
    id: int
    name: str
    description: str
    sku: str

    class Config:
        orm_mode = True
