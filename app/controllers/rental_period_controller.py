from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.schemas import rental_period as schemas
from app.services import rental_period_service
from app.database import get_db

router = APIRouter()


@router.post("/create", response_model=schemas.RentalPeriod)
def register(rental_period: schemas.RentalPeriodCreate, db: Session = Depends(get_db)):
    db_rental_period = rental_period_service.create_rental_period(
        db, rental_period)
    return db_rental_period


@router.get("/", response_model=list[schemas.RentalPeriod])
def get_rental_periods(db: Session = Depends(get_db)):
    rental_periods = rental_period_service.get_rental_periods(db)
    return rental_periods
