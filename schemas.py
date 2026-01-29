from pydantic import BaseModel, Field

class EmployeeCreate(BaseModel):
    name: str = Field(..., pattern="^[A-Za-z ]+$")
    address: str
    salary: float = Field(gt=0)
    age: int = Field(gt=0)

class EmployeeResponse(EmployeeCreate):
    id: int

    class Config:
        orm_mode = True
