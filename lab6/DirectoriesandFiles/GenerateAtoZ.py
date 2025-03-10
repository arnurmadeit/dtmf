import os
import string
output_dir = "alphabet_files"
os.makedirs(output_dir, exist_ok=True)
for letter in string.ascii_uppercase:
    filename = os.path.join(output_dir, f"{letter}.txt")
    with open(filename, 'w') as f:
        f.write(f"This file is under the letter {letter}")
    print(f"Created {filename}")