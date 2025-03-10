import os 

file_path = input("Enter the directory bro: ")

if os.path.exists(file_path):
    if os.access(file_path, os.W_OK):
        try:
            os.remove(file_path)
            print(f"{file_path} has been removed")
        except Exception as e: 
            print(f"Error deleting file {e}")
    else: 
        print("You do not have permission to the file")
else:
    print("The file does not exist") 