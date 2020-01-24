# Math Equation Solver

Math Equation Solver is a React webapp that solves handwritten mathematical equations. The current working application accepts a .jpg or .png file of a polynomial expression with integer coefficients and computes its roots. All back-end logic is developed from the ground up, with the current functionality of computing roots of polynomials.

The front-end application is developed using JavaScript and create-react-app, backed by Flask. Image to math conversion is implemented in Python using OCR technology with the MathPix API.  The parser and polynomial-solving algorithm, which uses Newton's method to compute roots, are implemented in C++ and ported to Python.

To run the app, make sure you have the proper packages installed and run ```npm run dev``` in the /client folder. 

Packages we used include:
 - concurrently
 - nodemon
 - bootstrap
 - jquery
