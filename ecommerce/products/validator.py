from sqlalchemy.orm import Session
from fastapi import HTTPException
from typing import Optional
from . models import Category

async def verify_category_exist(id: int, database: Session) -> Optional[Category]:
    category = database.query(Category).filter(Category.id == id).first()
    if not category:
        raise HTTPException(status_code=400, detail=f'Category with the id {id} is not available')
    
    return category