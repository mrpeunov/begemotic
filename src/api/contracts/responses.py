from pydantic import BaseModel


class AggrResultResponse(BaseModel):
    value: float
