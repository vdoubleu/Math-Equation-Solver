import sys
import base64
import requests
import json
import os
from dotenv import load_dotenv


# mathpix credentials 
def get_credentials():
    load_dotenv()
    endpoint = "https://api.mathpix.com/v3/latex"
    return os.getenv('APP_ID'), os.getenv('APP_KEY'), endpoint


# converts a base64 enocded image to a string in wolfram format
def to_wolfram(image_base64):

    image_uri = "data:image/jpg;base64," + image_base64
    app_id, app_key, endpoint = get_credentials()

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

if __name__ == "__main__":
    file_path = os.path.abspath('/home/cindyli/Pictures/math.jpg')
    print(to_wolfram("data:image/jpg;base64," + base64.b64encode(open(file_path, "rb").read()).decode()))