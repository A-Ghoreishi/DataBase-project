from sqlalchemy.orm import Session
from sqlalchemy import select
from . import models, schemas

# Users
def create_user(db: Session, payload: schemas.UserCreate) -> models.User:
    user = models.User(**payload.model_dump())
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def list_users(db: Session):
    return db.scalars(select(models.User).order_by(models.User.user_id)).all()

def get_user(db: Session, user_id: int):
    return db.get(models.User, user_id)

def update_user(db: Session, user: models.User, payload: schemas.UserUpdate):
    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(user, k, v)
    db.commit()
    db.refresh(user)
    return user

def delete_user(db: Session, user: models.User):
    db.delete(user)
    db.commit()

# Products 
def create_product(db: Session, payload: schemas.ProductCreate) -> models.Product:
    product = models.Product(**payload.model_dump())
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

def list_products(db: Session):
    return db.scalars(select(models.Product).order_by(models.Product.product_id)).all()

def get_product(db: Session, product_id: int):
    return db.get(models.Product, product_id)

def update_product(db: Session, product: models.Product, payload: schemas.ProductUpdate):
    data = payload.model_dump(exclude_unset=True)
    for k, v in data.items():
        setattr(product, k, v)
    db.commit()
    db.refresh(product)
    return product

def delete_product(db: Session, product: models.Product):
    db.delete(product)
    db.commit()
