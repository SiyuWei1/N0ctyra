# 1. You go to the local donation center to donate old clothes. This
# center will pay $3 per shirt, 5 dollars per pants, and $10 per jacket.
# In a Python snippet, prompt the user for the amount of each they will
# donate and output the amount of money they received.

# WRITE YOUR CODE FOR QUESTION 1 HERE
number_shirt = int(input("Number of shirts: "))
number_jacket = int(input("Number of jackets: "))
number_pant = int(input("Number of pants: "))
total = (3 * number_shirt) + (5 * number_jacket) + (10 * number_pant)
print("You will receive ", total, " dollars")

# 2. The average IST student takes 2 IST classes per semester. In a python
# snippet, prompt the user to enter a class name and the corresponding GPA
# as a float. Print out the classes with each corresponding grade and
# format the output.

# WRITE YOUR CODE FOR QUESTION 2 HERE
class1 = input("Class name #1: ")
grade1 = float(input("Grade #1: "))

class2 = input("Class name #2: ")
grade2 = float(input("Grade #2: "))

print(f"{class1:<12}{grade1:.2f}")
print(f"{class2:<12}{grade2:.2f}")

# 3. Prompt users to enter "pythonisgreat" (without the quotes). Output as
# three separate words.

# WRITE YOUR CODE FOR QUESTION 3 HERE
word = input("Enter 'pythonisgreat': ")

print("Word 1 is", word[0:6])
print("Word 2 is", word[6:8])
print("Word 3 is", word[8:])

# 4. Convert from meters to miles, feet, and inches. Prompt the user for
# the length in meters. Perform the calculations. Output the results
# of the calculation using 3 print statements. Format the output to 2
# decimal places. Use the following constants in your program:
#
# METERS_PER_MILE = 1609.34
# METERS_PER_FOOT = 0.3048
# METERS_PER_INCH = 0.0254

# WRITE YOUR CODE FOR QUESTION 4 HERE

METERS_PER_MILE = 1609.34
METERS_PER_FOOT = 0.3048
METERS_PER_INCH = 0.0254

meters = float(input("Length in meters: "))
miles = meters / METERS_PER_MILE
feet = meters / METERS_PER_FOOT
inches = meters / METERS_PER_INCH

print(f"Miles: {miles:.2f}")
print(f"Feet:  {feet:.2f}")
print(f"Inches:  {inches:.2f}")
