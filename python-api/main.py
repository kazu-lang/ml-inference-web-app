from fastapi import FastAPI
from app.schema import InferenceRequest, InferenceResponse
from app.inference import run_inference

app = FastAPI()
    
@app.post("/infer", response_model=InferenceResponse)
def infer(req: InferenceRequest):
    return run_inference(req)