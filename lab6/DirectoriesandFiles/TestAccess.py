import os
import sys 

parameter1 = os.access("meow.txt", os.F_OK)
print("Does the path exist?", parameter1)

parameter2 = os.access("meow.txt", os.R_OK)
print("Is the file readable?", parameter2)

parameter3 = os.access("meow.txt", os.W_OK)
print("Is the file writable?", parameter3)

parameter4 = os.access("meow.txt", os.X_OK)
print("Can I execute the file?", parameter4)