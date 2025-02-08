import math

def area():
    n = int(input("Input number of sides: "))
    l = int(input("Input the length of a side: "))

    ans = int((l**2 * n) / (4 * math.tan(math.pi/n)))

    return ans
print("The area of a polygon is: ", area())