from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProductAttributes(Base):
    __tablename__ = 'product_attributes'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    attribute_value_id = Column(Integer)
