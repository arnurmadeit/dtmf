def even_generator(n):
    for i in range(n + 1):
        if i % 2 == 0:
            yield i

if __name__ == "__main__":
    n = int(input("Enter n: "))
    
    evens = list(even_generator(n))
    
    print(",".join(str(num) for num in evens))
