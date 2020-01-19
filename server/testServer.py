from flask import Flask, request, jsonify, after_this_request

app = Flask(__name__)

@app.route('/hello', methods=['POST'])
def hello_world():
   @after_this_request
   def add_header(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   jsonResp = {'me':123, 'john':321}
   #print(jsonResp)
   print(request.data)
   return jsonify(jsonResp)

if __name__ == '__main__':
   app.run()

