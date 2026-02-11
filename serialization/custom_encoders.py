from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4

class ExampleModel(BaseModel):
    id: UUID
    timestamp: datetime

    class Config:
        json_encoders = {
            datetime: lambda v: v.isoformat()
        }
