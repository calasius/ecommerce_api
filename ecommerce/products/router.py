from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=['Products'], prefix='/products')

@router.post('/category', status_code=status.HTTP_201_CREATED)
async def create_category(request: schema.Category, database: Session = Depends(db.get_db)):
    category = await services.create_new_category(request, database)
    return category

@router.get('/category', response_model=List[schema.ListCategory])
async def get_all_categories(database: Session = Depends(db.get_db)):
    return await services.get_all_categories(database)

@router.get('/category/{id}', response_model=schema.ListCategory)
async def get_category_by_id(id: int, database: Session = Depends(db.get_db)):
    return await services.get_category_by_id(id, database)

@router.delete('/category/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_category_by_id(id: int, database: Session = Depends(db.get_db)):
    return await services.delete_category_by_id(id, database)

@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_new_product(request: schema.Product, database: Session = Depends(db.get_db)):
    return await services.create_new_product(request, database)

@router.get('/', response_model=List[schema.ProductListing])
async def get_all_products(database: Session = Depends(db.get_db)):
    return await services.get_all_products(database)