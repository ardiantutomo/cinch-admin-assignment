from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.services.product_service import create_product
from app.schemas.product_schema import ProductCreate, Product
from app.database import get_db

router = APIRouter()


@router.post("/", response_model=Product)
def create_product_endpoint(product_data: ProductCreate, db: Session = Depends(get_db)):
    try:
        return create_product(db, product_data)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
