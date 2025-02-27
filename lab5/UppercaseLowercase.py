import re

pattern = r"[A-Z]+[a-z]+"

SpiderMan = ["Adog", "AOSOSO", "21312", "Apooiiuyg", "absolutelyfuckinganything"]

for text in SpiderMan: 
    if re.fullmatch(pattern, text):
        print("YEAHHHHH")
    else:
        print("Fuck off")
