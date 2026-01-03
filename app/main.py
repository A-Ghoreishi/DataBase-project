from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db
from . import crud, schemas

app = FastAPI(
    title="Online Shop API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"   
)

@app.get("/health")
def health():
    return {"status": "ok"}

# Users
@app.post("/users", response_model=schemas.UserOut)
def create_user(payload: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_user(db, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/users", response_model=list[schemas.UserOut])
def list_users(db: Session = Depends(get_db)):
    return crud.list_users(db)

@app.get("/users/{user_id}", response_model=schemas.UserOut)
def get_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.put("/users/{user_id}", response_model=schemas.UserOut)
def update_user(user_id: int, payload: schemas.UserUpdate, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return crud.update_user(db, user, payload)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    crud.delete_user(db, user)
    return {"deleted": True}

# Products 
@app.post("/products", response_model=schemas.ProductOut)
def create_product(payload: schemas.ProductCreate, db: Session = Depends(get_db)):
    try:
        return crud.create_product(db, payload)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/products", response_model=list[schemas.ProductOut])
def list_products(db: Session = Depends(get_db)):
    return crud.list_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductOut)
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/products/{product_id}", response_model=schemas.ProductOut)
def update_product(product_id: int, payload: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return crud.update_product(db, product, payload)

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    crud.delete_product(db, product)
    return {"deleted": True}
