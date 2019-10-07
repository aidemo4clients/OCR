import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
for i in range(1,27):
    i=str(i)+'.png'
    file_name = os.path.abspath(i)

# Loads the image into memory
    with io.open(file_name, 'rb') as image_file:
        content = image_file.read()

        image = types.Image(content=content)

        # Performs label detection on the image file
        text_detection_response = client.text_detection(image=image)
        #print(text_detection_response)
        #print("====================================")
        annotations=text_detection_response.text_annotations
        #print(annotations)
        #print("|||||||||||||||||||||||||||||||||||||")
        if len(annotations) > 0:
            text = annotations[0].description
        else:
            text = ''
        #print('Extracted text {} from image ({} chars).'.format(text, len(text)))
        print(text)
        print("========")
    
