from fastapi import APIRouter
from starlette import status
from src.models.user import CreateUserRequest
from src.controllers.users import create


route = APIRouter(prefix="/v1/users")


@route.get("/")
async def get_users() -> str:
    return "testando"


@route.post("/create",
            status_code=status.HTTP_201_CREATED,
            tags=["users"],
            responses={400: {"description": "User Already Exists"}})
async def create_user(user_request: CreateUserRequest) -> str:
    create.handle(user_request)
    return {"message": "Usuário criado com sucesso"}
