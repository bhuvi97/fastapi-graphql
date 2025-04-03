import uvicorn
from fastapi import FastAPI

from config import app_config

from src.student.router import student_router

app = FastAPI(**app_config)
app.include_router(student_router)


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8083, reload=True)

