from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from src.models.sensor import Sensor


class Sample(BaseModel):
    id: Optional[str]
    sensor: Sensor
    value: float
    timestamp: datetime
