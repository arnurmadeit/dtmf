# Scope - area of visibility

""" 
python finds variables in the order of rule LEGB
local
enclosing
global
built-in
"""
def my_func():
    x = 10 # local variable
    print (x)

my_func()

print(next(gen)) # 1 
# print(x) # Error! Variable x is not visible outside of the function