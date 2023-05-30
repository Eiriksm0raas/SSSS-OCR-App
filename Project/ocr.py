import json
import cv2
import pytesseract
import urllib.request
import numpy as np
import time
from PIL import Image
#pytesseract.pytesseract.tesseract_cmd = r'C:\Users\halvo\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


class OCRConverter:

    def predict(self, url):
        image = self.url_to_image(url)
        preprocessed_image = self.preprocess_image(image)
        text = self.ocr(preprocessed_image)
        return text

    def crop_image(self, image):
        cropped_image = image[50:450, 100:500]
        return cropped_image

    def preprocess_image(self, image):
        # Crop the image by specifying the desired dimensions
        # cropped_image = image[50:450, 100:500]

        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        blur = cv2.GaussianBlur(gray, (5, 5), 0)
        thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        return thresh 
    
    def url_to_image(self, url):
        resp = urllib.request.urlopen(url)
        image = np.asarray(bytearray(resp.read()), dtype="uint8")
        image = cv2.imdecode(image, cv2.IMREAD_COLOR)
        return image

    def ocr(self, image):
        config = "--psm 6 -c tessedit_char_whitelist=\"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ%+- \""
        #config = "--psm 6 --oem 2 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1 tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ "
        #config = "--psm 6 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1"

        text = pytesseract.image_to_string(image, lang="eng+nor", config=config)
        return text
    
    def ocr2(self, image):
        config = "--psm 6"  # You can experiment with different PSM (page segmentation modes) values for better results
        text = pytesseract.image_to_string(image, lang="eng", config=config)
        return text

    def rotate_image(self, image):
        # Double transpose works best
        transposed_image = cv2.transpose(image)
        transposed_image = cv2.transpose(transposed_image)
        rotated_image = cv2.flip(transposed_image, 1)
        return cv2.transpose(rotated_image)

    def detect_and_correct_rotation(self, image):
        image = np.asarray(image)

        image = self.rotate_image(image)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Adaptive thresholding
        binary = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 15, 2)
        binary = cv2.bitwise_not(binary)
        coords = np.column_stack(np.where(binary > 0))
        angle = cv2.minAreaRect(coords)[-1]

        # Correct the angle
        if angle < -45:
            angle = -(90 + angle)
        else:
            angle = -angle

        # Compute new width and height
        h, w = image.shape[:2]
        new_w = int(abs(h * np.sin(np.radians(angle))) + abs(w * np.cos(np.radians(angle))))
        new_h = int(abs(h * np.cos(np.radians(angle))) + abs(w * np.sin(np.radians(angle))))
        M = cv2.getRotationMatrix2D((new_w / 2, new_h / 2), angle, 1.0)
        rotated = cv2.warpAffine(image, M, (new_w, new_h), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REPLICATE)

        return Image.fromarray(rotated)




