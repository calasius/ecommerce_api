from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session
from ecommerce import db
from . import schema
from . import services
from . import validator

router = APIRouter(tags=['Users'], prefix='/users')

async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.veryfy_user(request.email, database)

    if user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Email already registered')

    new_user = await services.new_user_register(request, database)
    return new_user