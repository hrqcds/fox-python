from src.database.db import get_host
from src.schema.user import users_schema


def execute():
    db = get_host()

    users = db.users

    list_users_mongo = users_schema(users.find())
    list_users = []

    for item in list_users_mongo:
        del item["password"]
        list_users.append(item)

    return list_users
