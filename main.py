from fastapi import FastAPI
from app.routes.user_routes import router as user_routes
from app.routes.attribute_routes import router as attribute_router
from app.routes.region_routes import router as region_router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(user_routes)
app.include_router(attribute_router)
app.include_router(region_router)


@app.get("/")
async def root():
    return {"message": "Hello World"}
