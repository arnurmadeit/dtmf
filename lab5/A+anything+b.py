import re

pattern = r"(a)+(.*)+b"

JeanMichelBasquiat = ("ayuikmnbgyuiokjhu9b", "asexvbolshomgorodeb", "987yhjl;;lmokokok", "Wookiepedia")

for text in JeanMichelBasquiat: 
    if re.fullmatch(pattern, text):
        print("Excelsior!")
    else:
        print("Death to industrial society")
    