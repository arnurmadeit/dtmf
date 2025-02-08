print(len([1, 2, 3])) # 3
print(max(10, 20, 30)) # 30

max = 10 # now max is a var, but not a function
# print(max(10, 20)) # Error! max is not a function anymore

del max # We delete var max
print(max(10, 20)) # 20

