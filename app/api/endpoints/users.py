from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.db.database import get_db
from app.db.models import User
from app.models.schemas import UserCreate, UserResponse
from app.core.security import get_password_hash

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(user_data: UserCreate, db: Session = Depends(get_db)):
    # Проверяем существующего пользователя
    existing_user = db.query(User).filter(User.email == user_data.email).first()
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Пользователь с таким email уже существует"
        )
    
    # Создаем пользователя
    user_db = User(
        name=user_data.name,
        age=user_data.age,
        email=user_data.email,
        hashed_password=get_password_hash(user_data.password)
    )

    # Сохраняем в БД
    db.add(user_db)
    db.commit()
    db.refresh(user_db)

    # Преобразуем для ответа
    user_response = UserResponse.from_orm(user_db)

    return user_response

# ДОБАВЛЯЕМ GET ЭНДПОИНТ
@router.get("/", response_model=List[UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    """Получить всех пользователей"""
    users = db.query(User).all()
    return users

@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """Получить пользователя по ID"""
    user_db = db.query(User).filter(User.id == user_id).first()
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Пользователь не найден"
        )
    
    return UserResponse.from_orm(user_db)