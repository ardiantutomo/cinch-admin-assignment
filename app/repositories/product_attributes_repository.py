from sqlalchemy.orm import Session
from app.models.product_attributes import ProductAttributes


def get_product_attribute_by_id(db: Session, attribute_id: int):
    return db.query(ProductAttributes).filter(ProductAttributes.id == attribute_id).first()


def create_product_attribute(db: Session, product_attribute: ProductAttributes):
    db.add(product_attribute)
    db.commit()
    db.refresh(product_attribute)
    return product_attribute


def get_all_product_attributes(db: Session):
    return db.query(ProductAttributes).all()
