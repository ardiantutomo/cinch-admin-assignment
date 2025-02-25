from sqlalchemy.orm import Session
from app.models.product_pricing import ProductPricing


def get_product_pricing_by_id(db: Session, pricing_id: int):
    return db.query(ProductPricing).filter(ProductPricing.id == pricing_id).first()


def create_product_pricing(db: Session, product_pricing: ProductPricing):
    db.add(product_pricing)
    db.commit()
    db.refresh(product_pricing)
    return product_pricing


def get_all_product_pricings(db: Session):
    return db.query(ProductPricing).all()
