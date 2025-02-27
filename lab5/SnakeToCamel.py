import re

def snake_to_camel(snake_str):
    def repl(match):
        return match.group(1).upper() 
    return re.sub(r'_([a-z])', repl, snake_str)

ouioui = input("What isss the sssnake ssstring?: ")

print(snake_to_camel(ouioui))