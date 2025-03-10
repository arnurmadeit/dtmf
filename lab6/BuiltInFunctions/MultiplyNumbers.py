import math

def multiply_list(numbers):
    return math.prod(numbers)

numbers = list(map(int, input("Aye throw me some numbers (separated by spaces boss): ").split()))
result = multiply_list(numbers)
print("Here comes Johnny: ", result)
