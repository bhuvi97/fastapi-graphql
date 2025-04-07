import strawberry
from datetime import date


@strawberry.type
class StudentType:
    id: int
    first_name: str
    last_name: str
    email: str
    dob: date
    phone_number: str
