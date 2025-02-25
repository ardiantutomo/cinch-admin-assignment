from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import attribute as schemas
from app.services import attribute_service
from app.database import get_db

router = APIRouter()


@router.post("/create", response_model=schemas.Attribute)
def register(attribute: schemas.AttributeCreate, db: Session = Depends(get_db)):
    db_attribute = attribute_service.create_attribute(db, attribute)
    return db_attribute


@router.get("/", response_model=list[schemas.Attribute])
def get_attributes(db: Session = Depends(get_db)):
    attributes = attribute_service.get_attributes(db)
    return attributes
