# Prompt the user for a number. Then find all the odd numbers from one to that number (inclusive), with each number printed on its own line.

num = int(input("Please enter a number: "))

for i in range(1, num+1, 2):
    print(i)

# A company wants to know the most common vowel in peoples' names. Using a while loop with a sentinel of "done",
# repeatedly prompt for a name and count the number of times each vowel is used. You can use any technique we
# have learned in class to perform the counting.


name = input("Please enter a name, or 'done' to quit: ")
while name != "done":
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    for char in name:
        if char == 'a':
            a += 1
        elif char == 'e':
            e += 1
        elif char == 'i':
            i += 1
        elif char == 'o':
            o += 1
        elif char == 'u':
            u += 1
    print("a:", a)
    print("e:", e)
    print("i:", i)
    print("o:", o)
    print("u:", u)
    name = input("Please enter a name, or 'done' to quit:")

# Prompt the user for the number of rows (x) and the number of columns (y).
# Then output a multiplication table containing X rows and Y columns.
# Your table should have right-aligned outputs for X and Y values up to 9.

row = int(input("How many rows do you want?: "))
column = int(input("How many columns do you want?: "))

for i in range(1, row + 1):
    for j in range(1, column + 1):
        print(f"{i * j:2}", end=" ")
    print()

# Write a Python program that prompts the user for a string.
# The program should use a for-loop to analyze each character and determine
# how many characters fall into each of the following categories:
#
# 1. Vowels (a, e, i, o, u — both uppercase and lowercase)
# 2. Consonants (letters that are not vowels)
# 3. Digits (0–9)
# 4. Whitespace (spaces, tabs, etc.)
# 5. Other characters (symbols, punctuation, etc.)

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





