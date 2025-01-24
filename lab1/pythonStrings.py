a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# python does not have the char data type, instead every symbol is a string of length 1
for x in "banana":
  print(x) # this is looping through a string, this outputs every letter in banana

#to get the length of a string, we just use : 
a = 'Hi mr Nurzhigit'
print(len(a))

#to check if a word or a substring exists in a string, we use print("smth" in stringname)

a = 'Teenage mutant ninja turtles

print("mutant" in a) # <-- this gives us True, cuz "mutant" exists in string a

#there is a similar function, but with print ("mutant" not in a)
