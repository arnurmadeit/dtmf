def my_generator():
    yield 1
    yield 2
    yield 3

gen = my_generator()
print(next(gen)) # 1 
print(next(gen)) # 2
print(next(gen)) # 3 
print(next(gen)) # 4

gen = example() 
print(next(gen)) 
print(next(gen)) 
