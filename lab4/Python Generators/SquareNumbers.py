def square_generator(n):
    for i in range(n + 1):
        yield i ** 2

# Example usage:
if __name__ == "__main__":
    N = int(input("Input a number please bro: "))
    for square in square_generator(N):
        print(square)
