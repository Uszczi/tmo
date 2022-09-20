from bson import ObjectId
from pydantic import BaseModel


class BaseApiResponse(BaseModel):
    class Config:
        json_encoders = {ObjectId: str}
