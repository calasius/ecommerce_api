from fastapi import HTTPException, status, Depends
from typing import List
from . import models
from . import schema
from . import validator
from sqlalchemy.orm import Session


async def create_new_category(request: schema.Category, database: Session):
    new_category = models.Category(name=request.name)
    database.add(new_category)
    database.commit()
    database.refresh(new_category)
    return new_category


async def get_all_categories(database: Session):
    return database.query(models.Category).all()


async def get_category_by_id(id: int, database: Session):
    category = database.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with the id {id} is not available",
        )
    return category


async def delete_category_by_id(id: int, database: Session):
    database.query(models.Category).filter(models.Category.id == id).delete()
    database.commit()


async def create_new_product(request: schema.Product, database: Session):
    await validator.verify_category_exist(request.category_id, database)
    new_product = models.Product(
        name=request.name,
        price=request.price,
        category_id=request.category_id,
        description=request.description,
        quantity=request.quantity,
    )
    database.add(new_product)
    database.commit()
    database.refresh(new_product)
    return new_product


async def get_all_products(database: Session) -> List[schema.Product]:
    return database.query(models.Product).all()
