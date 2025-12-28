from pydantic import BaseModel

class InferenceRequest(BaseModel):
    x: float
    
class InferenceResponse(BaseModel):
    result: float