from typing import Optional
from sqlalchemy.orm import Session
from . models import User

async def verify_email_exist(email: str, database: Session) -> Optional[User]:
    return database.query(User).filter(User.email == email).first()