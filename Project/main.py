from fastapi import FastAPI, Request, UploadFile, File, Response
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import StreamingResponse
from PIL import Image
import io
from ocr import OCRConverter
from camera_pi import Camera
import cv2
import numpy as np
from PIL import Image

camera = Camera()
camera.initialize()

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

converter = OCRConverter()

@app.get('/')
def root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get('/api/takepicture')
def takepicture():

    img = captureImage()
    return converter.ocr(img)
    
    
def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

def captureImage():
    frame_arr = np.frombuffer(camera.get_frame(), dtype=np.uint8)
    frame_img = cv2.imdecode(frame_arr, flags=cv2.IMREAD_COLOR)
    frame_img = cv2.cvtColor(frame_img, cv2.COLOR_BGR2RGB)
    return Image.fromarray(converter.preprocess_image(frame_img))

@app.get('/api/feed')
def feed():
    return StreamingResponse(gen(camera), media_type="multipart/x-mixed-replace;boundary=frame")

@app.post('/api/uploadpicture')
async def uploadpicture(file: UploadFile = File(...)):
    content = await file.read()
    image = Image.open(io.BytesIO(content))
    text = converter.ocr(image)
    return text

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, log_level="info", reload=True)
