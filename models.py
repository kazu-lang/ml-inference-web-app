from pydantic import BaseModel
from typing import Optional

class ApiResponse(BaseModel):
    """
    Standard API response wrapper.
    
    This model is used to unify all API responses.
    - status: indicates success or failure (e.g. "OK", "ERROR")
    - message: optional error or informational message
    - data: response payload (endpoint-specific)
    """
    status: str
    message: Optional[str] = None
    data: Optional[dict] = None

class InferRequest(BaseModel):
    """
    Request model for inference endpoint.
    
    Attributes:
        x(int): Input value for inference.
    """
    x: int
    
class InferResponse(BaseModel):
    """
    Response model for inference result.
    
    Attributes:
        result(int): Inference output value.
    """
    result: int