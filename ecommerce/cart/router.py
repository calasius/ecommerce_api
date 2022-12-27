from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.user.schema import User

from . import services
from . import schema

router = APIRouter(
    tags=["Cart"],
    prefix="/cart",
)

@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(product_id: int, database: Session = Depends(db.get_db)):
    result = await services.add_to_cart(product_id, database)
    return result

@router.get("/", response_model=schema.ShowCart)
async def get_all_cart_items(database: Session = Depends(db.get_db)):
    return await services.get_all_cart_items(database)
