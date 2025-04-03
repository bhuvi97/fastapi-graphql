from fastapi import APIRouter, Depends
from dependencies.sql_session import get_db
from sqlalchemy.ext.asyncio import AsyncSession

graphql_router = APIRouter(prefix="/graphql", tags=["graphql"])
