from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class ProductAttributes(Base):
    __tablename__ = 'product_attributes'

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'))
    attribute_value_id = Column(Integer, ForeignKey('attribute_values.id'))

    product = relationship("Product", back_populates="product_attributes")
    attribute_value = relationship(
        "AttributeValue", back_populates="product_attributes")
