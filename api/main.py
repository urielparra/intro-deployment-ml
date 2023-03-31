from fastapi import FastAPI
from .app.models import PredictionResponse, PredictionRequest
from .app.views import get_prediction

app = FastAPI(doc_url='/')

@app.post('/v1/prediction')
def  made_model_prediction(request: PredictionRequest):
    return PredictionResponse(worldwide_Gross=get_prediction(request))