from pydantic import BaseModel, EmailStr, Field, FieldValidationInfo, field_validator
from datetime import date
from typing import Optional


class Student(BaseModel):
    id: Optional[int] = Field(None)
    first_name: str = Field(None, max_length=50)
    last_name: str = Field(None, max_length=50)
    email: EmailStr
    dob: date = Field(..., description="Date of birth in YYYY-MM-DD format.")
    phone_number: str = Field(..., pattern=r'^\+?\d{10,15}$', description="Phone number must be 10 to 15 digits long and can include an optional '+' prefix.")

    @field_validator('dob')
    def validate_dob(cls, dob):
        today = date.today()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        if age < 18:
            raise ValueError('User must be at least 18 years old.')
        return dob
