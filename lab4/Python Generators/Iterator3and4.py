def divisibleby(n):
    for i in range(n):
        if i % 3 == 0 and i % 4 == 0 and i > 0:
            yield i

if __name__ == "__main__":
    n = int(input("Enter a number dawg: "))
    for number in divisibleby(n):
        print(number)