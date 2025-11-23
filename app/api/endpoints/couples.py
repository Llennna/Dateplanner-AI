from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.db.models import Couple, User  
from app.models.schemas import CoupleCreate, CoupleResponse  

router = APIRouter(prefix="/couples", tags=["couples"])

@router.post("/", response_model=CoupleResponse)
def create_couple(couple_data: CoupleCreate, db: Session = Depends(get_db)):
    user1 = db.query(User).filter(User.id == couple_data.user1_id).first()
    user2 = db.query(User).filter(User.id == couple_data.user2_id).first()
    
    if not user1 or not user2:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Один из пользователей не найден"
        )
    
    
    couple_db = Couple(
        user1_id=couple_data.user1_id,
        user2_id=couple_data.user2_id,
        couple_name=couple_data.couple_name,
        description=couple_data.description
    )
    
    db.add(couple_db)
    db.commit()
    db.refresh(couple_db)
    
    return CoupleResponse.from_orm(couple_db)