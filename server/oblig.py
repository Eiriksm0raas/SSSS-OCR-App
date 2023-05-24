import cv2
import pytesseract
import urllib.request
import numpy as np
import time

# Edit including cropping
def preprocess_image(image):
    # Crop the image by specifying the desired dimensions
    cropped_image = image[50:450, 100:500]

    gray = cv2.cvtColor(cropped_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    return thresh

# Originally preprocess_image
#def preprocess_image(image):
    #gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #blur = cv2.GaussianBlur(gray, (5, 5), 0)
    #thresh = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
    #return thresh

def ocr2(image):
    config = "--psm 6"  # You can experiment with different PSM (page segmentation modes) values for better results
    text = pytesseract.image_to_string(image, lang="eng", config=config)
    return text

# Added \"\" to the whitelist to include spacing.
def ocr(image):
    config = "--psm 6 -c tessedit_char_whitelist=\"ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ \""
    #config = "--psm 6 --oem 2 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1 tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789.,!?øåæØÅÆ "
    #config = "--psm 6 -c language_model_penalty_non_freq_dict_word=1 -c language_model_penalty_non_dict_word=1"


    text = pytesseract.image_to_string(image, lang="eng+nor", config=config)
    return text


def url_to_image(url):
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image

def takeimg():
    cap = cv2.VideoCapture(0)
    cv2.imshow("video",cap.read()[1])
    time.sleep(5)

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    ret, frame = cap.read()

    frame = cv2.rotate(frame, cv2.ROTATE_180)
    return frame

def img2():
    while True:
        ret, img=cap.read()
        img=cv2.flip(img, -1)
        #gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video',img)
        if cv2.waitKey(1) & 0xff == ord('q'):
            break
    return img

cap=cv2.VideoCapture(0)
cap.set(3,640) # Set Width
cap.set(4,480) # Set Height

url = "https://docs.unity3d.com/Packages/com.unity.textmeshpro@3.2/manual/images/TMP_RichTextLineIndent.png"
#image = url_to_image(url)
image = img2()
preprocessed_image = preprocess_image(image)
text = ocr(preprocessed_image)

print("Recognized text:\n", text)

cap.release()
cv2.destroyAllWindows()