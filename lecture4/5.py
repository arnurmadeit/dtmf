x = 5 
def change_x():
    global x 
    x = 10 # this is a local variable, not a changed version of global x
    print("Inside of the function: ", x)

change_x()
print("Outside: ", x)