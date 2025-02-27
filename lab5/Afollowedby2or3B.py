import re 

pattern = r'ab{2,3}'

textstr = ["abb", "abbb", "abbbb"]

for text in textstr:
    if re.fullmatch(pattern, text):
        print("Full match reached sir!")
    else:
        print("THis aint it dawg")