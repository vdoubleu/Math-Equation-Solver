# Math Equation Solver

Math Equation Solver is a React webapp that solves handwritten mathematical equations. The current working application accepts a .jpg or .png file and converts the image into a string representation of the mathematical equation. All back-end logic is developed from the ground up, with the current functionality of computing roots of polynomials.

The front-end application is developed using JavaScript and create-react-app, backed by Flask. Image to math conversion is implemented in Python using OCR technology with the MathPix API.  The parser and polynomial-solving algorithm, which uses Newton's method to compute roots, is implemented in C++.
