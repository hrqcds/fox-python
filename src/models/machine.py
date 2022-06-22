from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class Status(str, Enum):
    ON = "ON"
    MAINTENANCE = "MAINTENANCE"
    OFF = "OFF"


class AcquireDataBy(str, Enum):
    DATALOGGER = "DATALOGGER",
    MANUAL = "MANUAL",
    HYBRID = "HYBRID"


class MachineType(BaseModel):
    id: Optional[str]
    name: str
    description: Optional[str]
    created_at: datetime
    updated_at: datetime


class Machine(BaseModel):
    id: Optional[str]
    machine_code: str
    status: Status = Status.ON
    machine_type: MachineType
    created_at: datetime
    updated_at: datetime
