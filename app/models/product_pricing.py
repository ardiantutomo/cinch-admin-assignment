from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime
from app.database import Base

Base = declarative_base()


class ProductPricing(Base):
    __tablename__ = "product_pricings"

    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey('products.id'), index=True)
    rental_period_id = Column(Integer, ForeignKey(
        'rental_periods.id'), index=True)
    region_id = Column(Integer, ForeignKey('regions.id'), index=True)
    price = Column(Float, index=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.datetime.utcnow,
                        onupdate=datetime.datetime.utcnow)

    product = relationship("Product", back_populates="product_pricings")
    rental_period = relationship(
        "RentalPeriod", back_populates="product_pricings")
    region = relationship("Region", back_populates="product_pricings")
