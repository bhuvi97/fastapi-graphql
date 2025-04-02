from fastapi import APIRouter

student_router = APIRouter(prefix="/student", tags=["student"])

@student_router.get("", status_code=200)
async def student_signup():
    """
    This method creates an instance if student
    :return: id of the student created
    """
    pass
