def outer():
    x = "outer var" 

    def inner():
        print(x) # Access to var from enclosing scope

    inner() 

outer()