from sqlalchemy.orm import Session
from app.schemas import rental_period as schemas
from app.models.rental_period import RentalPeriod
from app.repositories import rental_period_repository
from fastapi import HTTPException


def create_rental_period(db: Session, rental_period: schemas.RentalPeriodCreate):
    db_rental_period = RentalPeriod(**rental_period.dict())
    if rental_period_repository.get_rental_period_by_months(db, db_rental_period.months):
        raise HTTPException(
            status_code=400, detail="Rental period already exists")
    return rental_period_repository.create_rental_period(db, db_rental_period)


def get_rental_periods(db: Session):
    return rental_period_repository.get_rental_periods(db)
