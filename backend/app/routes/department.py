from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.department import DepartmentCreate

from app.services.department_service import create_department
from app.services.department_service import get_departments

router = APIRouter(
    prefix="/departments",
    tags=["Departments"]
)


@router.get("/")
def list_departments(
        db: Session = Depends(get_db)
):

    return get_departments(db)


@router.post("/")
def add_department(
        department: DepartmentCreate,
        db: Session = Depends(get_db)
):

    return create_department(
        db,
        department.name
    )
