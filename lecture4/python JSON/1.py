# JSON - JavaScript Object Notation
import json
{ 
    "name": "Alice",
    "age": 25, 
    "city": "New York",
    "skills": ["Python", "JavaScript"]
}

# python object to JSON
data = {"name": "Alice", "age":25, "city": "New York"}

json_date = json.dumps(data)
print(json_date) 

