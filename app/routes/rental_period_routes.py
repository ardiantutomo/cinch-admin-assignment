from fastapi import APIRouter, Depends, Security
from app.controllers.rental_period_controller import router as rental_period_router
from app.auth import token_validation
from fastapi.security import HTTPBearer

api_key_header = HTTPBearer()
router = APIRouter()

router.include_router(
    rental_period_router, prefix="/rental_periods", tags=["rental_periods"], dependencies=[Depends(token_validation), Security(api_key_header)])
