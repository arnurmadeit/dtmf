import re 

pattern = r'(?=[A-Z]+)'

text = ["ABJIJHU", "ABCasdASD", "lkjhghjk"]

result = [re.sub(pattern, " ", word) for word in text]

print(result)