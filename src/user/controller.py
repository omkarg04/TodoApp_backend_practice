from src.user.dtos import UserSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException,status
from src.user.models import UserModel
from pwdlib import PasswordHash


password_hash = PasswordHash.recommended()


def get_password_hash(password):
    return password_hash.hash(password)



def register(body:UserSchema,db:Session):
    is_user = db.query(UserModel).filter(UserModel.username==body.username).first()
    if is_user:
        raise HTTPException(400,detail="User already exists")
    
    is_email = db.query(UserModel).filter(UserModel.email==body.email).first()
    if is_email:
        raise HTTPException(400,detail="Email already exists")

    hash_password = get_password_hash(body.password)

    new_user = UserModel(
        name = body.name,
        username = body.username,
        email = body.email,
        hash_password = hash_password 
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)



    return new_user
