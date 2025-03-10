import os
print("The working directory has these folders: ", os.listdir())

for dirpath, dirnames, filenames, in os.walk("."): 
    for dirname in dirnames: 
        print("Directory: ", os.path.join(dirpath, dirname))
    for filename in filenames:
        print("File: ", os.path.join(dirpath, filename))
