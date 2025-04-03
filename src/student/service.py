from sqlalchemy.ext.asyncio import AsyncSession
from src import models
from . import schemas
from sqlalchemy import select


async def create_student_user(student_data: schemas.Student, async_session: AsyncSession) -> int:
    """
    This method creates user in DB
    :param student_data: The student data
    :param async_session: The DB session
    :return: Created Student ID
    """
    new_user = models.Student(first_name=student_data.first_name, last_name=student_data.last_name,
                    email=student_data.email, dob=student_data.dob, phone_number=student_data.phone_number)
    async_session.add(new_user)
    await async_session.commit()
    return new_user.id


async def get_all_students(async_session: AsyncSession):
    """
    This method fetches aff the students from DB
    :param async_session: The DB session
    :return: List of all students
    """
    students = await async_session.execute(select(models.Student)).scalars().all()
    return students