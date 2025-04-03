import uvicorn
from fastapi import FastAPI

from config import app_config

from src.student.router import student_router
# from src.graphql.router import graphql_router
from graphene import Schema
from starlette_graphene3 import GraphQLApp

from src.graphql.service import Query

app = FastAPI(**app_config)
app.include_router(student_router, tags=["student"])
# app.include_router(graphql_router, tags=["graphql"])
schema = Schema(query=Query)
app.mount("/graphql", GraphQLApp(schema=schema))


@app.get("/", include_in_schema=True)
async def root():
    return {"Health": "OK"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8085, reload=True)

