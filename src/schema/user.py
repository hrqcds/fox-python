def user_schema(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "password": item["password"],
        "register": item["r"],
        "status": item["status"],
        "role": item["role"],
        "created_at": item["created_at"],
        "updated_at": item["updated_at"]
    }


def users_schema(entity) -> list:
    return [user_schema(item) for item in entity]
