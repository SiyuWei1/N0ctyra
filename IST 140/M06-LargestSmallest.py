/# Follow this PSEUDOCODE to code this program in Python:
#
# START
#
# Create an empty list called values
values = []
#
# PRINT "Please enter values, Q to quit:"
print("Please enter values, Q to quit:")
#
# READ userInput
userInput = input()
# WHILE userInput is not "Q" (ignore upper or lower case)
#     Convert userInput to a number
#     Add the number to values list
#     READ next userInput
# END WHILE
while userInput.upper() != "Q":
    num = int(userInput)
    values.append(num)
    userInput = input()
#
# Set largest to the first number in values
# Set smallest to the first number in values
largest = values[0]
smallest = values[0]
#
# FOR each number in values (starting from the second number)
#     IF number is greater than largest
#         Set largest to number
#     END IF
#     IF number is less than smallest
#         Set smallest to number
#     END IF
# END FOR
for number in values[1:]:
    if number > largest:
        largest = number
    if number < smallest:
        smallest = number
#
# FOR each number in values
#     PRINT the number
#     IF number is equal to largest
#         PRINT " <== largest value"
#     END IF
#     IF number is equal to smallest
#         PRINT " <== smallest value"
#     END IF
# END FOR
for number in values:
    if number == largest:
        print(f"{number}<==largest value")
    elif number == smallest:
        print(f"{number}<==smallest value")
    else:
        print(number)


#
# END

