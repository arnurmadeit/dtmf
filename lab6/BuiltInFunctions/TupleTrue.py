def allelementsttrue(t: tuple) -> bool:
    return all(t)

userinput = input("Enter numbers separated by spaces: ").strip()
t = tuple(map(int, userinput.split())) 

print(t)
print(allelementsttrue(t))
