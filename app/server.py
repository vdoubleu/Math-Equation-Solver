from flask import Flask, request, jsonify, after_this_request
from image_to_latex import to_wolfram

app = Flask(__name__)

@app.route('/imageCalc/', methods=['POST'])
def hello_world():
   @after_this_request
   def add_header(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   image_path = request.form['image_path']
   jsonResp = to_wolfram(image_path)
   return jsonResp

if __name__ == '__main__':
   app.run()