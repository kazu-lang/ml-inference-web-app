from fastapi import FastAPI, HTTPException
from models import InferRequest, InferResponse, ApiResponse
from inference import infer

app = FastAPI()
    
@app.post("/infer", response_model=ApiResponse)
def run_infer(request: InferRequest):
    if request.x < 0:
        raise HTTPException(
            status_code=400,
            detail="x must be non-negative"
        )
    
    result = infer(request.x)
    return ApiResponse(
        status="OK",
        data=InferResponse(result=result).dict()
    )