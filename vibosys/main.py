from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from db import SessionLocal, engine
import models, schemas

models.Base.metadata.create_all(bind=engine)
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/product/add", response_model=schemas.ProductResponse)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    new_product = models.Product(**product.dict())
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@app.get("/product/list", response_model=list[schemas.ProductResponse])
def list_products(db: Session = Depends(get_db), skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

@app.get("/product/{id}/info", response_model=schemas.ProductResponse)
def get_product(id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == id).first()
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.put("/product/{id}/update", response_model=schemas.ProductResponse)
def update_product(id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    existing_product = db.query(models.Product).filter(models.Product.id == id).first()
    if not existing_product:
        raise HTTPException(status_code=404, detail="Product not found")
    for key, value in product.dict().items():
        setattr(existing_product, key, value)
    db.commit()
    db.refresh(existing_product)
    return existing_product
