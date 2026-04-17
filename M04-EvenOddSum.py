##
# Prompt the user to enter a series of values.

# Determine and print the number of even values and the
# number of odd values entered by the user.
# Accumulate the total sum of the numbers and print it

even_count =  0
odd_count = 0
total = 0
inputStr = input("Enter an integer (blank line to quit): ")
while inputStr != "":
    value = int(inputStr)
    total += value
    if value % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    inputStr = input("Enter an integer (blank line to quit): ")

print(f"The user entered {even_count} even values and {odd_count} odd values.")
print(f"The cumulative total is {total}")
