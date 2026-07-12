from datetime import date

from pydantic import BaseModel


class AllocationCreate(BaseModel):

    asset_id: int

    employee_id: int

    expected_return: date


class AllocationResponse(BaseModel):

    id: int

    asset_id: int

    employee_id: int

    status: str

    class Config:
        from_attributes = True
