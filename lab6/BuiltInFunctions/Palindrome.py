def is_palindrome(s: str) -> bool:
    s = ''.join(filter(str.isalnum, s)).lower()
    
    return s == s[::-1]

string = input("Enter a string: ")
if is_palindrome(string):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
