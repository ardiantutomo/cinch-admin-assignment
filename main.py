from fastapi import FastAPI

app = FastAPI(port=9000)


@app.get("/")
async def root():
    return {"message": "Hello World"}