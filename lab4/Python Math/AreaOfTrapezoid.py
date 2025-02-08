import math

def area():
    h = int(input("Height: "))
    a = int(input("Base, first value: "))
    b = int(input("Base, second value: "))

    ans = (a + b)*h/2

    return ans
print("Expected Output: ", area())