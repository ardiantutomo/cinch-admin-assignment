from sqlalchemy.orm import Session
from app.schemas import user as schemas
from app.models.user import User
from app.repositories import user_repository
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def create_user(db: Session, user: schemas.UserCreate):
    hashed_password = pwd_context.hash(user.password)
    db_user = User(name=user.name, email=user.email, password=hashed_password, role="admin")
    return user_repository.create_user(db, db_user)

def authenticate_user(db: Session, email: str, password: str):
    user = user_repository.get_user_by_email_and_admin_role(db, email)
    if not user or not pwd_context.verify(password, user.password):
        return False
    return user 