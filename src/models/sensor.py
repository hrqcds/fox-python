from enum import Enum
from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field


class SensorType(BaseModel):
    name: str
    description: str
    unittest: str


class Sensor(BaseModel):
    id: Optional[str]
    sensor_type: SensorType
    offset: float
    created_at: datetime
    updated_at: datetime
