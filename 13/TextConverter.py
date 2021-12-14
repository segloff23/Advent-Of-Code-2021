
import io;
from os import environ;
from google.cloud import vision
from PIL.Image import fromarray;
from numpy import array;

def readArrayAsText(data):
    
    environ['GOOGLE_APPLICATION_CREDENTIALS'] = "./gcloudAuth.json";

    img = fromarray(array(data, dtype="uint8"));
    imgByteArr = io.BytesIO();
    img.save(imgByteArr, format="BMP");
    imgByteArr = imgByteArr.getvalue();
    
    client = vision.ImageAnnotatorClient();
    image = vision.Image(content=imgByteArr);
    response = client.text_detection(image=image);

    return response.text_annotations[0].description.strip();
