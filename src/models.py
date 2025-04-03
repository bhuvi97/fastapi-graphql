from sqlalchemy import Column, Integer, String, Date, Sequence
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    dob = Column(Date, nullable=True)  # Date of Birth as Date
    phone_number = Column(String(15), nullable=False)