from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from .model_loader import get_answer
import os

app = FastAPI(title="Question Answering API")

# Mount static files
app.mount("/ui", StaticFiles(directory="app/ui"), name="ui")

class QuestionRequest(BaseModel):
    context: str
    question: str

class AnswerResponse(BaseModel):
    answer: str
    confidence_score: float

@app.post("/ask", response_model=AnswerResponse)
async def ask_question(request: QuestionRequest):
    try:
        result = get_answer(request.context, request.question)
        return AnswerResponse(**result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
async def root():
    return FileResponse('app/ui/index.html')
