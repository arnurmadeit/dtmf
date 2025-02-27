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

result = re.findall(pattern, text_to_match) 
print(result) # prints the list of string elements 

# print(result.group()) # print the match as the string 

