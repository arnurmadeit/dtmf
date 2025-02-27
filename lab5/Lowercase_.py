import re

pattern = r"[a-z]+_[a-z]+"

UltraMan = ["asd_ghjkjhghj", "awd_hwiw", "ABC_", "128", "afefefoo_ww"]

for text in UltraMan: 
    if re.fullmatch(pattern, text):
        print("Aye aye captain!")
    else:
        print("This aint it lil bro")
