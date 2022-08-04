from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.user import Status, User
from src.models.machine import Machine


class Process(BaseModel):
    id: Optional[str]
    name: str
    insertBy: str
    status: Status = Status.ACTIVE
    users: Optional[List[User]]
    machines: Optional[List[Machine]]
    created_at: datetime
    updated_at: datetime
