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
    await async_session.flush()
    await async_session.refresh(new_user)
    await async_session.commit()
    return new_user.id


async def get_all_students(async_session: AsyncSession, id: int = None):
    """
    This method fetches aff the students from DB
    :param id: The id of the student
    :param async_session: The DB session
    :return: List of all students
    """
    sql_stmt = select(models.Student)
    if id:
        sql_stmt = sql_stmt.filter(models.Student.id == id)
    students = await (async_session.execute(sql_stmt))
    student_scalars = students.scalars().all()
    return student_scalars