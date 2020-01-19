from flask import Flask, request, jsonify, after_this_request
from image_to_latex import to_wolfram

app = Flask(__name__)

@app.route('/<image_path>', methods=['GET'])
def hello_world(image_path):
   @after_this_request
   def add_header(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   jsonResp = to_wolfram(image_path)
   return jsonResp

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)
