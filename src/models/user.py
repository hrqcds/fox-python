from enum import Enum
from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field


class Status(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Role(str, Enum):
    ADMIN = "ADMIN"
    OPERATOR = "OPERATOR"


class User(BaseModel):
    id: Optional[str]
    name: str
    password: str
    r: str = Field(None, alias="register")
    status: Status
    role: Role
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True


class CreateUserRequest(BaseModel):
    name: str
    r: str = Field(None, alias="register", max_length=13, min_length=13, description="Matricula do colaborador")
    password: str = Field(None, min_length=6, description="Senha do colaborador")
    status: Status = Status.ACTIVE
    role: Role = Role.OPERATOR

    class Config:
        orm_mode = True
