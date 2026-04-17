##
# 1. Write a Python snippet to output the digits 0 - 9.
# Output each digit to a separate line.
# Use a while loop to control iterations.
# zyBooks reference: chapter 4.1

# WRITE YOUR CODE FOR QUESTION 1 HERE

i = 0
while i < 10:
    print(i)
    i += 1

# 2. Prompt the user for a series of floating point numbers, followed by a -1 to quit.
# Determine and output the minimum value.
# Use a while loop to control iterations.
# zyBooks reference: chapters 4.5, 4.6, and 4.9

# WRITE YOUR CODE FOR QUESTION 2 HERE


number = float(input("Enter a floating point number, or -1 to quit: "))
min = number

while number != -1:
    if number < min:
        min = number
    number = float(input("Enter a floating point number, or -1 to quit: "))
    
print(f"The minimum is {min:.1f}")

# 3. Prompt the user for a series of floating point numbers, followed by a -1 to quit.
# Determine and output the minimum, maximum, average, and range of numbers (the difference between
# the maximum and the minimum). Use a while loop to control iterations.
# zyBooks reference: chapter 4.9

# WRITE YOUR CODE FOR QUESTION 3 HERE

number = float(input("Enter a floating point number, or -1 to quit: "))

if number != -1:
    min_val = number
    max_val = number
    total = 0.0
    count = 0
    
    while number != -1:
        count += 1
        total += number
        if number < min_val:
            min_val = number
        if number > max_val:
            max_val = number

        number = float(input("Enter a floating point number, or -1 to quit: "))

    print(f"The minimum is {min_val:.1f}")
    print(f"The maximum is {max_val:.1f}")
    print(f"The average is {total / count:.1f}")
    print(f"The range is {max_val - min_val:.1f}")
