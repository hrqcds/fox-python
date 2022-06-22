from src.database.db import get_host
from src.schema.user import user_schema
from bson import ObjectId
from fastapi import HTTPException
from starlette import status


def execute(user_id: str):
    db = get_host()

    users = db.users

    try:
        user = user_schema(users.find_one({"_id": ObjectId(user_id)}))
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found")

    return user
