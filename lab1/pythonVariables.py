x = 5
y = "John" #here, we can either use double quotes or single quotes, thankfully it doesn't matter 
print(x)
print(y)
#apparently, variable can change type after they are declared, and the type does not need to be declared as well

#we can also use casting

x = str(3)
y = int(3)
z = float(3)

#variables are case-sensitive, so A =/= a
#also, we can get their type by 
print(type(x))

# moreover, we can assign many values to multiple variables, or equate them all to one value, or unpack a collection. This is shown below. 

"""
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)
"""

# also, we can use the print function in many different ways (note that string + int cannot be output)
x = 5
y = 10
print(x + y)

# or we could use 

x = 5
y = 10
print(x, y)

# using functions and the keyword "global", we can dabble with global variables 

x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
