import json
import cv2
import pytesseract
import urllib.request
import numpy as np
import time
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


class OCRConverter(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OCRConverter, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        pass

    def predict(self, url):
        image = self.url_to_image(url)
        preprocessed_image = self.preprocess_image(image)
        text = self.ocr(preprocessed_image)
        print(text)
        return text

    def preprocess_image(self, image):
        # Crop the image by specifying the desired dimensions
        # cropped_image = image[50:450, 100:500]
        cropped_image = image

        gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return thresh 
    
    def url_to_image(self, url):
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def ocr(self, image):
        config = "--psm 6 -c tessedit_char_whitelist=\"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ \""
        #config = "--psm 6 --oem 2 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1 tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ "
        #config = "--psm 6 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1"


        text = pytesseract.image_to_string(image, lang="eng+nor", config=config)
        return text
    
    def ocr2(self, image):
        config = "--psm 6"  # You can experiment with different PSM (page segmentation modes) values for better results
        text = pytesseract.image_to_string(image, lang="eng", config=config)
        return text



