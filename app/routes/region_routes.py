from fastapi import APIRouter, Depends, Security
from app.controllers.region_controller import router as region_router
from app.auth import token_validation
from fastapi.security import HTTPBearer

api_key_header = HTTPBearer()
router = APIRouter()

router.include_router(
    region_router, prefix="/regions", tags=["regions"], dependencies=[Depends(token_validation), Security(api_key_header)])
