import re 
# Write a Python program to split a string at uppercase letters.

pattern = r'(?=[A-Z])'

text = "HeyGuysWassupSkiSkiSkiMaskTheSlumpGodOhMyGod"

answ = re.split(pattern, text)

print(answ)