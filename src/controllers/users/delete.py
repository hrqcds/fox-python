from src.database.db import get_host
from fastapi import HTTPException
from starlette import status
from bson import  ObjectId
from src.schema.user import user_schema


def execute(user_id: str):
    db = get_host()

    db_users = db.users

    if user_id is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="params not found")

    try:
        user = user_schema(db_users.find_one_and_delete({"_id": ObjectId(user_id)}))
    except Exception:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="user not exist")

    return "Usuário deletado com sucesso"

