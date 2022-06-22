from pymongo import MongoClient
from src.models.user import CreateUserRequest
from fastapi import HTTPException
from starlette import status
from passlib.hash import sha256_crypt
from datetime import datetime
from src.database.db import get_host


def handle(user_request: CreateUserRequest) -> None:
    db = get_host()
    db_user = db.users
    new_user = dict(user_request)

    try:
        user_exist = db_user.find_one({"register": new_user["r"]})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Lost host communication")

    if user_exist is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="User Already Exists")

    new_user["password"] = sha256_crypt.encrypt(new_user["password"])
    new_user["created_at"] = datetime.now()
    new_user["updated_at"] = datetime.now()

    db_user.insert_one(new_user)
