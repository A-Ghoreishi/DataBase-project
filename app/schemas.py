from pydantic import BaseModel, EmailStr
from typing import Optional

# Users
class UserCreate(BaseModel):
    full_name: str
    email: EmailStr
    password_hash: str
    phone: Optional[str] = None
    role: str = "customer"

class UserUpdate(BaseModel):
    full_name: Optional[str] = None
    phone: Optional[str] = None
    role: Optional[str] = None

class UserOut(BaseModel):
    user_id: int
    full_name: str
    email: EmailStr
    phone: Optional[str]
    role: str

    class Config:
        from_attributes = True

# Products
class ProductCreate(BaseModel):
    category_id: Optional[int] = None
    name: str
    sku: str
    price: float
    stock_qty: int
    description: Optional[str] = None
    is_active: bool = True

class ProductUpdate(BaseModel):
    category_id: Optional[int] = None
    name: Optional[str] = None
    price: Optional[float] = None
    stock_qty: Optional[int] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None

class ProductOut(BaseModel):
    product_id: int
    category_id: Optional[int]
    name: str
    sku: str
    price: float
    stock_qty: int
    description: Optional[str]
    is_active: bool

    class Config:
        from_attributes = True
