from fastapi import APIRouter, Depends
import strawberry
from dependencies.sql_session import get_db
from sqlalchemy.ext.asyncio import AsyncSession
from .service import Query
from strawberry.fastapi import GraphQLRouter


schema = strawberry.Schema(query=Query)
graphql_app = GraphQLRouter(schema=schema, graphiql=True, context_getter=lambda request : {"db": next(get_db())})
