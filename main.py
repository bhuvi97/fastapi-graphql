import uvicorn
from fastapi import FastAPI

from config import app_config

app = FastAPI(**app_config)


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8083, reload=True)

