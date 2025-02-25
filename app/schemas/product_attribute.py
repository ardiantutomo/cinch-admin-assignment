from pydantic import BaseModel
from datetime import datetime


class ProductAttribute(BaseModel):
    id: int
    product_id: int
    attribute_value_id: int
    created_at: datetime
    updated_at: datetime
