from sqlalchemy.orm import Session
from app.schemas import attribute as schemas
from app.models.attribute import Attribute
from app.repositories import attribute_repository
from fastapi import HTTPException


def create_attribute(db: Session, attribute: schemas.AttributeCreate):
    db_attribute = Attribute(**attribute.model_dump())
    if attribute_repository.get_attribute_by_name(db, db_attribute.name):
        raise HTTPException(status_code=400, detail="Attribute already exists")
    return attribute_repository.create_attribute(db, db_attribute)


def get_attributes(db: Session):
    return attribute_repository.get_attributes(db)
