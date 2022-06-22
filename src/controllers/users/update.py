from src.database.db import get_host
from src.models.user import UpdateUserRequest
from fastapi import HTTPException
from starlette import status
from bson import ObjectId
from datetime import datetime

def execute(user_id: str, data: UpdateUserRequest):
    db = get_host()

    db_users = db.users

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user id not found")

    try:
        db_users.find_one({"_id": ObjectId(user_id)})
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not found")

    user = dict(data)
    user["updated_at"] = datetime.now()

    db_users.find_one_and_update({"_id": ObjectId(user_id)}, {"$set": dict(user)})

    return "usuário atualizado com sucesso"
