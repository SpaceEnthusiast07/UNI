import sympy as sp

# Create the symbolic variables for the equation
x = sp.symbols('x')

expr1 = x**2 + 2
expr2 = 2*x + 3

expr3 = expr1 + expr2

print(expr3)