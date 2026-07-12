from pydantic import BaseModel


class DepartmentCreate(BaseModel):

    name: str


class DepartmentResponse(BaseModel):

    id: int

    name: str

    status: bool

    class Config:

        from_attributes = True
