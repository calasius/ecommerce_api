from fastapi import HTTPException, status
from . import models
from . import schema
from sqlalchemy.orm import Session

async def new_user_register(request: schema.User, database: Session) -> models.User:
    new_user = models.User(name=request.name, email=request.email, password=request.password)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def all_users(database: Session) -> models.User:
    return database.query(models.User).all()

async def get_user_by_id(id: int, database: Session) -> models.User:
    user = database.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with the id {id} is not available')
    return user

async def delete_user_by_id(id: int, database: Session):
    database.query(models.User).filter(models.User.id == id).delete()
    database.commit()
