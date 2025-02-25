from fastapi import APIRouter, Depends, Security
from app.controllers.attribute_controller import router as attribute_router
from app.auth import token_validation
from fastapi.security import HTTPBearer


api_key_header = HTTPBearer()
router = APIRouter()

router.include_router(
    attribute_router, prefix="/attributes", tags=["attributes"], dependencies=[Depends(token_validation), Security(api_key_header)])
