# Write a Python program to write a list to a file.
l = ['Harvey', 'Dent']
with open("meow.txt", 'w') as f: 
    for items in l:
        f.write(f"{items}\n")

    print("File written successfully")