str = input("Enter a string: ")
vowels = 0
consonants = 0
digits = 0
whitespace = 0
other = 0

for char in str:
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
        vowels += 1
    elif char.isalpha():
        consonants += 1
    elif char.isdigit():
        digits += 1
    elif char.isspace():
        whitespace += 1
    else:
        other += 1

print("vowels:", vowels)
print("consonants:", consonants)
print("digits:", digits)
print("whitespace:", whitespace)
print("other:", other)
