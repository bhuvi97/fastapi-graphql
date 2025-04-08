
from graphene import String, ObjectType, Int, Date, List, Field
from dependencies.sql_sync_session import get_db_sync
from src.models import Student as StudentModel


class StudentType(ObjectType):
    id = Int()
    first_name = String()
    last_name = String()
    dob = Date()
    email = String()
    phone_number = String()

class Query(ObjectType):
    all_students = List(StudentType)

    def resolve_all_students(self, info):
        request = info.context["request"]
        token = request.headers.get("authorization")
        print(token)
        db_gen = get_db_sync()
        db = next(db_gen)
        try:
            students = db.query(StudentModel).all()
            return students
        finally:
            db.close()



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