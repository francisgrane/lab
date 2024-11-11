# microservice1.py
from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import SessionLocal
import requests

app = FastAPI()

@app.post("/analyze_text")
async def analyze_text(text: str, db: Session = Depends(SessionLocal)):
    response = requests.post("https://<azure-ai-endpoint>/text-analysis", json={"text": text})
    analysis_result = response.json()
    db.execute("INSERT INTO text_analyses (text, result) VALUES (:text, :result)", {"text": text, "result": analysis_result})
    db.commit()
    return {"result": analysis_result}
