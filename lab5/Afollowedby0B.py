import re

pattern = r'ab*'

test_strings = ["a", "ab", "abb", "abbbb", "b", "ac", ""]

for text in test_strings:
    if re.fullmatch(pattern, text):
        print(f"'{text}' matches the pattern.")
    else:
        print(f"'{text}' does not match the pattern.")
