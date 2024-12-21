from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserUpdate, UserResponse
from app.services.users_service import get_user, get_users, create_user, update_user, delete_user
from app.session import get_db

router = APIRouter()

@router.get("/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db)):
    return update_user(db, user_id, user_update)

@router.delete("/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db)):
    delete_user(db, user_id)
    return {"detail": "User deleted successfully"}