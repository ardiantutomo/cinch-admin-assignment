from fastapi import FastAPI
from app.routes.user_routes import router as user_routes
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()
app.include_router(user_routes)

@app.get("/")
async def root():
    return {"message": "Hello World"}