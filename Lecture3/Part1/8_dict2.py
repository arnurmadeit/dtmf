# Dictionaries

ourdict = {
    "make": "BMW", 
    "model": "M5 E34", 
    "year": 1995, 
    "color": "Black"
}

# print(ourdict)
# print(type(ourdict))

ourdict["mileage"] = 100000
ourdict.update({"price" : "8 million tenge"})

# print(ourdict)

# for key in ourdict:
#    print(key, ourdict[key])

for value in ourdict.values():
    print(value)

for key, value in ourdict.items():
    print(key, value)