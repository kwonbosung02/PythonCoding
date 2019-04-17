from sympy import Symbol,solve,symbols
import pprint
x = Symbol('x')
y = Symbol('y') 
#equation = 2 * x -6
#equation = x ** 2 + 3*x + 1

a,b,c = symbols('a,b,c')
#equation = a*x**2 + b*x + c

equation1 = x + 2 * y - 3 
equation2 = 3 * x - y + 2

#print(solve(equation,x,dict=True))
print(solve((equation1,equation2),dict=True))