
from graphene import String, ObjectType


class Query(ObjectType):
    hello = String(name=String(default_value="World"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


"""
class Student(SQLAlchemyObjectType):
    class Meta:
        model = StudentModel
        interfaces = (relay.Node, )


class Query(ObjectType):
    node = relay.Node.Field()
    all_students = SQLAlchemyConnectionField(Student.connection)


import strawberry
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from fastapi import Depends
from dependencies.sql_session import get_db
from ..models import Student
from strawberry.fastapi import GraphQLRouter
from .graphql_types import StudentType


@strawberry.type
class Query:
    @strawberry.field
    async def all_users(self, info) -> list[StudentType]:
        async_session: AsyncSession = info.context["db"]
        result = await async_session.execute(select(Student))
        return result.scalars().all()
"""