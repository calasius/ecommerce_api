from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from typing import List

from ecommerce import db
from . import services
from . import schema

router = APIRouter(tags=["Orders"], prefix="/orders")


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schema.ShowOrder)
async def initiate_order_processing(database: Session = Depends(db.get_db)):
    return await services.initiate_order(database)


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[schema.ShowOrder])
async def order_list(database: Session = Depends(db.get_db)):
    return await services.get_order_listing(database)
