# Write a Python program that validates user passwords using the following three functions:
# 1. eightCharacters() - validates that the password has at least 8 characters
# 2. oneUpperOneLower() - validates that the password has at least one uppercase and one lowercase letter
# 3. oneDigit() - validates that the password has at least one digit
# In the code below, replace the code that says WRITE YOUR CODE HERE, but keep the remaining code.

# WRITE YOUR CODE HERE
def eightCharacters(password):
    return len(password) >= 8
def oneUpperOneLower(password):
    upper = False
    lower = False
    for i in password:
        if i.isupper():
            upper = True
        if i.islower():
            lower = True
    return upper and lower
def oneDigit(password):
    digit = False
    for i in password:
        if i.isdigit():
            digit = True
    return digit


print("eightCharacters(\"abcdefgh\"):\t", eightCharacters("abcdefgh"))
print("eightCharacters(\"python\"):\t\t", eightCharacters("python"))
print("eightCharacters(\"test case #3\"):", eightCharacters("test case #3"))
print()
print("oneUpperOneLower(\"HiThere\"):\t", oneUpperOneLower("HiThere"))
print("oneUpperOneLower(\"psuforever\"):\t", oneUpperOneLower("psuforever"))
print("oneUpperOneLower(\"THON2026\"):\t", oneUpperOneLower("THON2026"))
print()
print("oneDigit(\"HiThere\"):\t", oneDigit("HiThere"))
print("oneDigit(\"psuforever\"):\t", oneDigit("psuforever"))
print("oneDigit(\"THON2026\"):\t", oneDigit("THON2026"))


# Write a program that asks for a phrase, then asks again to confirm it.
# Create a function, same_phrase(), which checks if the phrases match.
# If the phrases don't match, prompt again. If the phrases still don't match,
# output "Error: You must enter matching phrases." and stop program execution.

def same_phrase(phrase1, phrase2):
    return phrase1 == phrase2


phrase1 = input("Enter a phrase: ")
phrase2 = input("Enter the same phrase: ")
if not same_phrase(phrase1, phrase2):
    phrase1 = input("Enter a phrase: ")
    phrase2 = input("Enter the same phrase: ")
    if not same_phrase(phrase1, phrase2):
        print("Error: You must enter matching phrases.")



# Write a code snippet to prompt a user for their age. Next, ask the user how many times
# they would like their age to be repeated (i.e., printed on screen). Pass these values
# as parameters to an age_repeater() function, which does not return a value.

def age_repeater(age, times):
    for i in range(times):
        print(age)


age = int(input("Enter your age: "))
times = int(input("How many times would you like that repeated: "))
age_repeater(age, times)


# New management has taken over and is offering to take 25% off your current rent if you share a room
# Use a function, rent_calculation(), to take arguments representing the current rent, whether or
# not you share a room, and the current electric bill. rent_calculation() should not return any value, but
# should print the total cost with a dollar sign and two decimals of precision.

def rent_calculation(rent, share, electrice):
    if share == "Y":
        total = rent * 0.75 + electrice
    else:
        total = rent + electrice
    print("Your average monthly cost is: ", f"${total:.2f}")

rent = int(input("How much is your monthly rent? "))
share = input("Do you share a room (Y/N)?")
electrice = int(input("How much is your average electric bill? "))
rent_calculation(rent, share, electrice)
