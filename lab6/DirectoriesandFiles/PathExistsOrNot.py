import os

path = input("Enter the file or directory path: ")

if os.path.exists(path):
    print(f"Path exists: {path}")
    
    directory = os.path.dirname(path)
    print(f"Directory portion: {directory}")
    
    filename = os.path.basename(path)
    print(f"Filename portion: {filename}")
else:
    print("The path does not exist.")
