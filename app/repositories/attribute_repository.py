from sqlalchemy.orm import Session
from app.models.attribute import Attribute


def get_attribute_by_name(db: Session, name: str):
    return db.query(Attribute).filter(Attribute.name == name).first()


def create_attribute(db: Session, attribute: Attribute):
    db.add(attribute)
    db.commit()
    db.refresh(attribute)
    return attribute


def get_attributes(db: Session):
    return db.query(Attribute).all()
