from fastapi import APIRouter, Depends
import strawberry
from dependencies.sql_session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from .service import Query
from strawberry.fastapi import GraphQLRouter


async def get_context(request):
    db_gen = get_db()
    db = await anext(db_gen)
    return {"db": db}

schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema=schema, graphiql=True, context_getter=get_context)
