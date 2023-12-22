from fastapi import FastAPI
from transformers import pipeline
from pydantic import BaseModel

class Item(BaseModel):
    text: str

app = FastAPI()
classifier = pipeline("sentiment-analysis")

@app.get("/")
def root():
    """Test message"""
    return {"message": "Welcome to the app!"}

@app.post("/predict/")
def predict(item: Item):
    """Предсказание тональности текста"""
    return classifier(item.text)[0]
