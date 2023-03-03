# SSSS-OCR-App
api, website and OCR for the course Sustainability through smart systems

# Start instructions

### Pip packages
- pip install tensorflow --user
- pip install keras-ocr --user
- pip install "fastapi[all]"

### Server
In once console do:
- cd server
- uvicorn main:app --reload
> --reload is just for auto refresh

### Client
In another console do:
- cd client
- npm install
> npm install only first time
- npm run dev
