# Write a Python snippet to validate user input. Prompt for a string with a length between
# 4 and 12 characters and continuously repeat the loop until a valid length is inputted. Output the valid string.


while True:
    s = input("Enter a string between 4 and 12 characters in length: ")
    if 4 <= len(s) <= 12:
        break
print("Valid string: success")

# Using a nested for-loop, create these shapes
#        *
#        * *
#        * * *
#        * * * *
#        * * * * *
#
#        * * * * *
#        * * * *
#        * * *
#        * *
#        *

for i in range(1,6):
    for j in range(i):
        print("*",end=" ")
    print()

print()

for i in range(5,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()

# Prompt the user to enter quiz grades for IST 140, using a while loop that stops when the user enters -1.
# As you enter grades, keep track of the minimum, maximum, and average, and print them when the user
# has finished entering the grades.
#
# Then, do the same for IST 242 with separate variables. After both classes’ grades are entered,
# compare the statistics and print which class has the higher maximum, lower minimum, and higher average.

grade = int(input("Enter a quiz grade for IST 140 (-1 to stop): "))
total_140 = grade
count_140 = 1
max_140 = grade
min_140 = grade

while grade != -1:
    total_140 += grade
    count_140 += 1
    if grade < min_140:
        min_140 = grade
    if grade > max_140:
        max_140 = grade
    grade = int(input("Enter a quiz grade for IST 140 (-1 to stop): "))
average_140 = total_140 / count_140

print(f"\nIST 140 minimum grade: {min_140}")
print(f"IST 140 maximum grade: {max_140}")
print(f"IST 140 average grade: {average_140}")

grade = int(input("Enter a quiz grade for IST 242 (-1 to stop): "))
total_242 = grade
count_242 = 1
max_242 = grade
min_242 = grade

while grade != -1:
    total_242 += grade
    count_242 += 1
    if grade < min_242:
        min_242 = grade
    if grade > max_242:
        max_242 = grade
    grade = int(input("Enter a quiz grade for IST 242 (-1 to stop): "))
average_242 = total_242 / count_242

print(f"\nIST 242 minimum grade: {min_242}")
print(f"IST 242 maximum grade: {max_242}")
print(f"IST 242 average grade: {average_242}")

if max_242> max_140:
    print("IST 242 had the higher maximum")
else:
    print("IST 140 had the higher minimum")
if min_242> min_140:
    print("IST 140 had the lower minimum")
else:
    print("IST 242 had the lower maximum")
if average_242> average_140:
    print("IST 242 had the higher average")
else:
    print("IST 140 had the higher average")

# Most security professionals say that a password should have at least: 1) an uppercase letter, 2) a lowercase letter,
# and 3) a digit. Ask the user to input a password and output whether each requirement has been met or not.
# At the end, print out whether the password meets all requirements or not.
# Use a loop and if statements; do not use any programming concepts which we have not learned in class.

password = input("Enter your password: ")

upper = False
lower = False
digit = False

for i in password:
    if i.isupper():
        upper = True
    if i.islower():
        lower = True
    if i.isdigit():
        digit = True

print(f"1. Uppercase letter: {upper}")
print(f"2. Lowercase letter: {lower}")
print(f"3. Digit: {digit}")

print(f"\nAll password requirements are met: {upper and lower and digit}")




