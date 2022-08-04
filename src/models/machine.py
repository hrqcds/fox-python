from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.sensor import Sensor


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


class Machine(BaseModel):
    id: Optional[str]
    machine_code: str
    status: Status = Status.ON
    machine_type: MachineType
    sensors: Optional[List[Sensor]]
    created_at: datetime
    updated_at: datetime
