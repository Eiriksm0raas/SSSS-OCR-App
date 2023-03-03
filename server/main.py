from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import json

from ocr import OCRConverter

converter = OCRConverter()

app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return { "Endpoints": {
        "GET": [
            "/api/read/"
        ]
    } }

@app.get("/api/read/")
async def convertImgFromUrl(img_url: str):
    return json.loads(converter.predict(img_url))

@app.post("/api/upload/")
async def convertImgFromUpload(file: UploadFile):
    return { 'hello': file.filename }