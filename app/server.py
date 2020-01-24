from flask import Flask, request, jsonify, after_this_request
from image_to_latex import to_wolfram
from polynomial_solver import solve

app = Flask(__name__)

@app.route('/imageCalc/', methods=['POST'])
def hello_world():
   @after_this_request
   def add_header(response):
      response.headers.add('Access-Control-Allow-Origin', '*')
      return response

   image_path = request.form['image_path']
   wolfram_string = to_wolfram(image_path)
   solutions = solve(wolfram_string)
   if len(solutions) == 0:
      solutions = 'No solutions'
   return solutions

if __name__ == '__main__':
   app.run()
