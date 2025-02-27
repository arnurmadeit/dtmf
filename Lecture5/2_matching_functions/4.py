# What are regular expressions?

# Introduction to regex with easy exercises:
# https://regexone.com/lesson/introduction_abcs 

# Guide to python regex
# https://regexone.com/references/python

# Python regex HOWTO - tutorial for python regexes
# https://docs.python.org/3/howto/regex.html

# Online regex engine to test regexes, supports python flavour
# https://regex101.com/#python

# w3schools tutorial for regexes
# https://www.w3schools.com/python/python_regex.asp 

import re 

text_to_match = "John's email is john.doe@example.com, and his backup is johndoe123@work.net" 

pattern = '[Jj]ohn' # our regex 

results = re.finditer(pattern, text_to_match) 

print(results) # iterator with match objects 

for result in results:
    print(result)


