from fastapi import APIRouter, Depends
from dependencies.sql_session import get_db
from . import schemas
from . import service
from sqlalchemy.ext.asyncio import AsyncSession

student_router = APIRouter(prefix="/student", tags=["student"])

@student_router.post("", include_in_schema=True, status_code=201)
async def student_signup(student_data: schemas.Student, async_session: AsyncSession = Depends(get_db)) -> int:
    """
    This is the router method for saving the students
    :param student_data: The Student data
    :param async_session: The db session
    :return: The student id
    """
    return await service.create_student_user(student_data=student_data, async_session=async_session)


@student_router.get("", include_in_schema=True, status_code=200)
async def get_students(async_session: AsyncSession = Depends(get_db)) -> int:
    """
    This is the router method for fetching all the students
    :param async_session: The db session
    :return: The list of students
    """
    return 1000
