import uvicorn
from fastapi import FastAPI

from config import app_config

from src.student.router import student_router
from src.graphql.router import graphql_app
from middleware.auth_middleware import auth_middleware

app = FastAPI(**app_config)
app.include_router(student_router, tags=["student"])
# app.include_router(graphql_router, tags=["graphql"])
app.middleware("http")(auth_middleware)
app.mount("/graphql", graphql_app)


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)

