def count_case_letters(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

text = input("Enter a string: ")
upper, lower = count_case_letters(text)

print("Uppercase Letters:", upper)
print("Lowercase Letters:", lower)
