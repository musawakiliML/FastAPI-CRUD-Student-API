from typing import Optional
from pydantic import BaseModel, EmailStr, Field


class StudentSchema(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    course_of_study: str = Field(...)
    year: int = Field(..., gt=0, lt=9)
    gpa: float = Field(..., le=4.0)
    
    
    class Config:
        schema_extra = {
            "example":{
                "fullname" : "John Doe",
                "email" : "johnd@x.edu.ng",
                "course_of_study" : "Computer Science",
                "year": 4,
                "gpa": "3.56",
            }
        }
        
        
class UpdateStudentSchema(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    course_of_study: Optional[str]
    year: Optional[int]
    gpa: Optional[float]
    
    
    class Config:
        schema_extra = {
            "example":{
                "fullname" : "John Doe",
                "email" : "johnd@x.edu.ng",
                "course_of_study" : "Computer Science and Engineering",
                "year": 4,
                "gpa": "3.80",
            }
        }
        
        
def ResponseModel(data, message):
    return {
        "data": [data],
        "code": 200,
        "message": message,
    }
    

def ErrorResponseModel(error, code, message):
    return {
        "error": error,
        "code": code,
        "message": message
    }