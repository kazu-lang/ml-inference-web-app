from pydantic import BaseModel

class InferRequest(BaseModel):
    x: int
    
class InferRequest(BaseModel):
    result: int