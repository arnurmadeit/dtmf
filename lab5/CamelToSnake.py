import re

def camel_to_snake(camel_str):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', camel_str).lower()

camel_case_str = "helloWorldExample"
snake_case_str = camel_to_snake(camel_case_str)
print(snake_case_str) 
