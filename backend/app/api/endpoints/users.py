from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.users import UserCreate, UserUpdate, UserResponse
from app.services.users_service import get_user, get_users, create_user, update_user, delete_user
from app.session import get_db
from app.services.auth_service import get_current_user
from app.db.models.users import User

router = APIRouter()


@router.get("/me")
def read_current_user(current_user: User = Depends(get_current_user)):
    return {
        "id": current_user.id,
        "first_name": current_user.firstName,
        "second_name": current_user.secondName,
        "email": current_user.email,
        "role": current_user.role,
        "position": current_user.position,
    }


@router.get("/", response_model=list[UserResponse])
def list_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Admin","RH"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    return get_users(db, skip=skip, limit=limit)

@router.get("/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Admin","RH"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    db_user = get_user(db, user_id)
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@router.post("/", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Admin"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    return create_user(db, user)

@router.put("/{user_id}", response_model=UserResponse)
def update_existing_user(user_id: int, user_update: UserUpdate, db: Session = Depends(get_db),current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Employee","RH"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    return update_user(db, user_id, user_update)

@router.delete("/{user_id}")
def delete_existing_user(user_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role not in ["Admin"]:
        raise HTTPException(status_code=403, detail="Access forbidden: insufficient permissions")
    delete_user(db, user_id)
    return {"detail": "User deleted successfully"}