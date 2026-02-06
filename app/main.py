from fastapi import FastAPI, UploadFile, File
from app.models import TextRequest
from app.nlp import analyzeText


app = FastAPI(title='Document NLP Serivice')

@app.get('/')
def health():
    return {"status":'running'}

@app.post('/analyze')
def analyze(req: TextRequest):
    return analyzeText(req.text)

@app.post("/upload")
async def upload(file: UploadFile = File (...)):
    content = await file.read()
    text = content.decode("utf-8", errors='ignore')
    return analyzeText(text)