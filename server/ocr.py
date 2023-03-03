import keras_ocr
import json


class OCRConverter(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(OCRConverter, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.pipeline = keras_ocr.pipeline.Pipeline()

    def predict(self, url):
        converted = self.pipeline.recognize([keras_ocr.tools.read(url)])[0]
        result = []
        for data in converted:
            result.append({
                data[0]: data[1].tolist()
            })
        return json.dumps(result)

    
    
    