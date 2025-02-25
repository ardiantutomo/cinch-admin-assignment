from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import datetime

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
