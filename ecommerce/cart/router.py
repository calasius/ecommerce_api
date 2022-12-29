from fastapi import APIRouter, Depends, status, Response
from sqlalchemy.orm import Session

from ecommerce import db
from ecommerce.user.schema import User
from ecommerce.auth.jwt import get_current_user

from . import services
from . import schema

router = APIRouter(
    tags=["Cart"],
    prefix="/cart",
)


@router.post("/add", status_code=status.HTTP_201_CREATED)
async def add_product_to_cart(
    product_id: int,
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    result = await services.add_to_cart(product_id, database, current_user)
    return result


@router.get("/", response_model=schema.ShowCart)
async def get_all_cart_items(
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    return await services.get_all_cart_items(database, current_user)


@router.delete("/{cart_item_id}", status_code=status.HTTP_204_NO_CONTENT)
async def remove_cart_item_by_id(
    cart_item_id: int,
    database: Session = Depends(db.get_db),
    current_user: User = Depends(get_current_user),
):
    await services.remove_cart_item_by_id(cart_item_id, database, current_user)
