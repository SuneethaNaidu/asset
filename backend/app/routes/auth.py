from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.database import get_db

from app.schemas.user import UserRegister
from app.schemas.user import UserLogin

from app.services.user_service import create_user
from app.services.user_service import get_user_by_email

from app.auth.password import verify_password
from app.auth.jwt_handler import create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/signup")
def signup(
    user: UserRegister,
    db: Session = Depends(get_db)
):

    existing = get_user_by_email(
        db,
        user.email
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    new_user = create_user(
        db,
        user.full_name,
        user.email,
        user.password
    )

    return {
        "success": True,
        "message": "User Registered Successfully",
        "user": {
            "id": new_user.id,
            "name": new_user.full_name,
            "email": new_user.email
        }
    }


@router.post("/login")
def login(
    credentials: UserLogin,
    db: Session = Depends(get_db)
):

    user = get_user_by_email(
        db,
        credentials.email
    )

    if user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid Email"
        )

    if not verify_password(
        credentials.password,
        user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid Password"
        )

    token = create_access_token(
        {
            "sub": user.email
        }
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }
