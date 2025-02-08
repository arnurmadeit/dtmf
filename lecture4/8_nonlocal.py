def outer():
    x = 5

    def inner():
        nonlocal x
        x = 10 # Now we are changing x in outer scope 
        print("Inside inner: ", x)
        
    inner() 
    print("Inside outer: ", x) # 5 (outer x did not change)

outer()