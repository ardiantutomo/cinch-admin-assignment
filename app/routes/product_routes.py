from fastapi import APIRouter, Depends, Security
from app.controllers.product_controller import router as product_router
from app.auth import token_validation
from fastapi.security import HTTPBearer

api_key_header = HTTPBearer()
router = APIRouter()

router.include_router(
    product_router, prefix="/products", tags=["products"], dependencies=[Depends(token_validation), Security(api_key_header)])
