from fastapi import FastAPI
from app.schema import InferenceRequest, InferenceResponse
from app.inference import run_inference
from inference import infer

app = FastAPI()
    
@app.post("/infer", response_model=InferenceResponse)
def infer(request: InferenceRequest):
    result = infer(request.x)
    return {"result": result}