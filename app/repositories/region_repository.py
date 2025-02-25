from sqlalchemy.orm import Session
from app.models.region import Region


def get_region_by_name(db: Session, name: str):
    return db.query(Region).filter(Region.name == name).first()


def create_region(db: Session, region: Region):
    db.add(region)
    db.commit()
    db.refresh(region)
    return region


def get_regions(db: Session):
    return db.query(Region).all()
