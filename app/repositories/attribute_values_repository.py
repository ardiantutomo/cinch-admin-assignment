from sqlalchemy.orm import Session
from app.models.attribute_value import AttributeValue


def get_attribute_value_by_id(db: Session, value_id: int):
    return db.query(AttributeValue).filter(AttributeValue.id == value_id).first()


def create_attribute_value(db: Session, attribute_value: AttributeValue):
    db.add(attribute_value)
    db.commit()
    db.refresh(attribute_value)
    return attribute_value


def get_all_attribute_values(db: Session):
    return db.query(AttributeValue).all()
