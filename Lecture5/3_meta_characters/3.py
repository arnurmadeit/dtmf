# metacharacters
# . ^ $ * + ? { } [ ] \ | ( )
# . - any symbol
# ^ - matches at the beginning of the string 
# $ - matches at the end of the string
# * - quantifier, 0 or more repititions 
# + - quantifier, 1 or more repititions
# ? - quantifier, 0 or 1 repitiion
# {} - quantifier, allows to specify the exact amount of repititions
# [] - set of characters 
# \ - backslash, used for special sequences or escaping characters
# | - or, allows to check for 2 or more patterns 
# () - grouping 

import re

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net" 

pattern = r'email|backup' # our regex 
# 3 last symbols at the end of the string

result = re.findall(pattern, text_to_match)

print(result) 
