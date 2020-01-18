import sys
import base64
import requests
import json
import os
from dotenv import load_dotenv


# mathpix credentials 
load_dotenv()
app_id = os.getenv('APP_ID')
app_key = os.getenv('APP_KEY')

endpoint = "https://api.mathpix.com/v3/latex"


def to_wolfram(image_uri):

    request_params = {
    "src": image_uri,
    "ocr": ["math", "text"], 
    "formats": [
        "wolfram"
        ]
    }

    r = requests.post(endpoint,
        data=json.dumps(request_params),
        headers={"app_id": app_id, "app_key": app_key,
                "Content-type": "application/json"})
    return json.loads(r.text)["wolfram"]


# test
if __name__ == "__main__":
    file_path = os.path.abspath('/home/cindyli/Pictures/handwritten-note.jpg')
    img_base64 = "data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()
    equation = to_wolfram(img_base64)
    print(equation.replace(' ', ''))
