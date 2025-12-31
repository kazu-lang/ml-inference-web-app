from pydantic import BaseModel
from typing import Optional

class ApiResponse(BaseModel):
    status: str
    message: Optional[str] = None
    data: Optional[dict] = None

class InferRequest(BaseModel):
    x: int
    
class InferResponse(BaseModel):
    result: int