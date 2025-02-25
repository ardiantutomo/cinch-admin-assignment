from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import region as schemas
from app.services import region_service
from app.database import get_db

router = APIRouter()


@router.post("/create", response_model=schemas.Region)
def register(region: schemas.RegionCreate, db: Session = Depends(get_db)):
    db_region = region_service.create_region(db, region)
    return db_region


@router.get("/", response_model=list[schemas.Region])
def get_regions(db: Session = Depends(get_db)):
    regions = region_service.get_regions(db)
    return regions
