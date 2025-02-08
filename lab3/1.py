# convertation from grams to ounces

def gram_to_ounce(grams):
    return grams / 28.3495231

grams = float(input("Enter the grams: "))

print(f'{grams} grams is equal to {gram_to_ounce(grams)} ounces')