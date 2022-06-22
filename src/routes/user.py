from fastapi import APIRouter
from starlette import status
from src.models.user import CreateUserRequest, UpdateUserRequest
from src.controllers.users import create, find_all, find_by_id, update, delete

route = APIRouter(prefix="/v1/users")


@route.get("/", tags=["users"])
async def get_users() -> list:
    list_uses = find_all.execute()
    return list_uses


@route.get("/find/{user_id}", tags=["users"])
async def get_user(user_id: str) -> dict:
    user = find_by_id.execute(user_id)
    return user


@route.post("/create",
            status_code=status.HTTP_201_CREATED,
            tags=["users"],
            responses={400: {"description": "User Already Exists"}})
async def create_user(user_request: CreateUserRequest) -> str:
    create.handle(user_request)
    return {"message": "Usuário criado com sucesso"}


@route.put("/update/{user_id}", status_code=status.HTTP_200_OK, tags=["users"])
async def update_user(user_id: str, data: UpdateUserRequest):
    return update.execute(user_id, data)


@route.delete("/delete/{user_id}", status_code=status.HTTP_200_OK, tags=["users"])
async def delete_user(user_id: str):
    return  delete.execute(user_id)
