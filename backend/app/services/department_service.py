from sqlalchemy.orm import Session

from app.models.department import Department


def get_departments(db: Session):

    return db.query(Department).all()


def create_department(
        db: Session,
        name: str
):

    department = Department(
        name=name
    )

    db.add(department)

    db.commit()

    db.refresh(department)

    return department
