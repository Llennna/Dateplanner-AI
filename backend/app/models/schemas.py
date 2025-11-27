from pydantic import BaseModel, Field, EmailStr
from datetime import datetime
from typing import List, Optional

# ==================== USER SCHEMAS ====================

class UserCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, examples=["Левая"])
    age: int = Field(..., ge=18, le=100, examples=[21])
    email: EmailStr = Field(..., examples=["leva@example.com"])
    password: str = Field(..., min_length=6, examples=["securepassword"])

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    email: str
    
    class Config:
        from_attributes = True


# ==================== COUPLE SCHEMAS ====================

class CoupleCreate(BaseModel):
    user1_id: int = Field(..., examples=[1])
    user2_id: int = Field(..., examples=[2])
    couple_name: str = Field(..., examples=["Левая и Лена"])
    description: Optional[str] = Field(None, examples=["Самая крутая пара!"])

class CoupleResponse(BaseModel):
    id: int
    user1_id: int
    user2_id: int
    couple_name: str
    description: Optional[str]
    created_at: datetime
    
    class Config:
        from_attributes = True


# ==================== DATE PREFERENCE SCHEMAS ====================

class DatePreferenceCreate(BaseModel):
    couple_id: int = Field(..., examples=[1])
    place_types: List[str] = Field(..., examples=[["ресторан", "парк"]])
    budget_level: str = Field(..., examples=["среднее"])
    min_rating: float = Field(4.0, ge=0, le=5, examples=[4.5])
    description: str = Field(..., examples=["Хочу романтическое место с видом"])
    location: str = Field(..., examples=["Москва"])

class DatePreferenceResponse(BaseModel):
    id: int
    couple_id: int
    place_types: List[str]
    budget_level: str
    min_rating: float
    description: str
    location: str
    created_at: datetime
    
    class Config:
        from_attributes = True


# ==================== DATE RECOMMENDATION SCHEMAS ====================

class DateRecommendation(BaseModel):
    place_name: str = Field(..., examples=["Ресторан 'Панорама'"])
    address: str = Field(..., examples=["ул. Примерная, 123"])
    rating: float = Field(..., ge=0, le=5, examples=[4.7])
    price_level: str = Field(..., examples=["среднее"])
    description: str = Field(..., examples=["Романтический ресторан с видом на город"])
    coordinates: Optional[tuple[float, float]] = Field(None, examples=[(55.7558, 37.6173)])


# ==================== AUTH SCHEMAS ====================

class LoginRequest(BaseModel):
    email: str = Field(..., examples=["leva@example.com"])
    password: str = Field(..., examples=["securepassword"])

class Token(BaseModel):
    access_token: str
    token_type: str