from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ecommerce import db
from ecommerce.auth.jwt import get_current_user
from . import services
from . import schema

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initiate_order_processing(
    database: Session = Depends(db.get_db),
    current_user=Depends(get_current_user),
):
    return await services.initiate_order(database, current_user)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def order_list(
    database: Session = Depends(db.get_db),
    current_user=Depends(get_current_user),
):
    return await services.get_order_listing(database, current_user)
