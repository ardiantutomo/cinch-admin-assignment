from sqlalchemy.orm import Session
from app.models.rental_period import RentalPeriod


def get_rental_period_by_months(db: Session, months: int):
    return db.query(RentalPeriod).filter(RentalPeriod.months == months).first()


def create_rental_period(db: Session, rental_period: RentalPeriod):
    db.add(rental_period)
    db.commit()
    db.refresh(rental_period)
    return rental_period


def get_rental_periods(db: Session):
    return db.query(RentalPeriod).all()
