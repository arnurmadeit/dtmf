import time
import math

def meowmeow(num: float, delay_ms: int):
    print(f"Waiting for {delay_ms} milliseconds....")
    result = math.sqrt(num)
    time.sleep(delay_ms/1000)
    return result

num = int(input("Enter number: "))
delay_ms = int(input("Enter delay in milliseconds: "))
print(meowmeow(num, delay_ms))


