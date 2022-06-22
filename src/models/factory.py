from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.Process import Process


class Factory(BaseModel):
    id: Optional[str]
    name: str
    process: List[Process]
    created_at: datetime
    updated_at: datetime
