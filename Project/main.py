from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
from ocr import OCRConverter

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

converter = OCRConverter()

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/api/takepicture')
def takepicture():
    return "hello"

@app.post('/api/uploadpicture')
async def uploadpicture(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    text = converter.ocr(image)
    return text
