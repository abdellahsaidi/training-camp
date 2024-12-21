"""from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from app.services.auth_service import authenticate_user, create_access_token
from app.session import get_db

router = APIRouter()

@router.post("/login", response_model=dict)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/register", response_model=dict)
def register_new_user(user: UserCreate, db: Session = Depends(get_db)):
    create_user(db, user)
    return {"detail": "User registered successfully"}

@router.post("/logout", response_model=dict)
def logout_user():
    return {"detail": "User logged out successfully"}"""