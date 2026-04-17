# 1. Write a Python snippet that prompts the user to enter an IST course number;
# it must be exactly one of the following: 140, 242, 261, 311, or 411.
# Use If/elif/else to determine whether they entered a valid course number.
# If invalid, print "Invalid." If valid, print the title of the class, using the following key:
# 140: Intro to Application Development
# 242: Intermediate & Object-Oriented Application Development
# 261: Application Development Design Studio I
# 311: Object-Oriented Design and Software Applications
# 411: Distributed-Object Computing

# WRITE YOUR CODE FOR QUESTION 1 HERE
course = int(input("Enter a valid IST course number: "))

if course == 140:
    print("Intro to Application Development")
elif course == 242:
    print("Intermediate & Object-Oriented Application Development")
elif course == 261:
    print("Application Development Design Studio I")
elif course == 311:
    print("Object-Oriented Design and Software Applications")
elif course == 411:
    print("Distributed-Object Computing")
else:
    print("Invalid")



# 2. Write a Python snippet that prompts a user to input a number between 1 - 100.
# Then output if the number is well below average (<20), below the average (<40),
# in the average (between 40 and 60), above the average (>60), or well above average (>80).
# If none of these, then print "Invalid."

# WRITE YOUR CODE FOR QUESTION 2 HERE
num = int(input("Enter a number between 1 and 100:"))

if 0 < num < 20:
    print("well below average")
elif 20 <= num < 40:
    print("below the average")
elif 40 <= num <= 60:
    print("in the average")
elif 60 < num <= 80:
    print("above the average")
elif 80 < num <= 100:
    print("well above average")
else:
    print("Invalid")


# 3. Prompt for three integers. Check to see if all three are even, and print either "All even"
# or "Not all even."

# WRITE YOUR CODE FOR QUESTION 3 HERE
num1 = int(input("Enter the first integer:"))
num2 = int(input("Enter the second integer:"))
num3 = int(input("Enter the third integer:"))

if num1 %2 == 0 and num2 %2 == 0 and num3 %2 == 0:
    print("All even")
else:
    print("Not all even.")



# 4. Write a program that calculates and prints the value of the coupon a person
# can receive based on groceries purchased using the table below.
# Prompt the user for the money spent of their groceries, as a float.
# Print the value of the coupon to two decimal places of precision.
# Greater than or equal to $210: coupon is 14%
# Greater than or equal to $150: coupon is 12%
# Greater than or equal to $60: coupon is 10%
# Greater than or equal to $10: coupon is 8%
# Less than $10: no coupon

# WRITE YOUR CODE FOR QUESTION 4 HERE
spent = float(input("Enter the amount spent on groceries: "))

if spent >= 210:
    coupon = spent * 0.14
elif 150 <= spent < 210:
    coupon = spent * 0.12
elif 60 <= spent < 150:
    coupon = spent * 0.10
elif 10 <= spent < 60:
    coupon = spent * 0.08
else:
    coupon =0.0

print(f"The coupon amount is ${coupon:.2f}")
