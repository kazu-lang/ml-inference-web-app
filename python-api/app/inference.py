from app.schema import InferenceRequest, InferenceResponse

def run_inference(req: InferenceRequest) -> InferenceResponse:
    #仮推論ロジック
    result = req.x * 2
    return InferenceResponse(result=result)