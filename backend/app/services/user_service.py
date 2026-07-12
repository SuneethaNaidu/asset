from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.password import hash_password


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def create_user(db: Session, full_name: str, email: str, password: str):
    user = User(
        full_name=full_name,
        email=email,
        password_hash=hash_password(password),
        role_id=4,  # Default Employee Role
        status=True
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user
