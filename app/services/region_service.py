from sqlalchemy.orm import Session
from app.schemas import region as schemas
from app.models.region import Region
from app.repositories import region_repository
from fastapi import HTTPException


def create_region(db: Session, region: schemas.RegionCreate):
    db_region = Region(**region.dict())
    if region_repository.get_region_by_name(db, db_region.name):
        raise HTTPException(status_code=400, detail="Region already exists")
    return region_repository.create_region(db, db_region)


def get_regions(db: Session):
    return region_repository.get_regions(db)
