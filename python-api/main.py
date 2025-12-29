from fastapi import FastAPI
from app.schema import InferenceRequest, InferenceResponse
from app.inference import run_inference
from logic import simple_inference

app = FastAPI()
    
@app.post("/infer", response_model=InferenceResponse)
def infer(x: int):
    result = simple_inference(x)
    return {"result": result}