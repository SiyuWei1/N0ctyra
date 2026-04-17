# Copy and paste these instructions to the top of your program as a comment, and then write a program to do what the instructions say: Write a program that computes and displays the perimeter of a letter-size (8.5 × 11 inch) sheet of paper and the length of its diagonal.
import math

# Hint: to find the length of the diagonal, use the Pythagorean theorem; this is expressed by the formula a² + b² = c², where 'a' and 'b' are the lengths of the legs, and 'c' is the length of the hypotenuse. Python can help you calculate square roots; see the "Mathematical Functions" section in zyBooks chapter 2.2 for a refresher.

# Your output should match the following; note that two decimal points of precision are displayed:

# Perimeter: 39.00
# Diagonal: 13.90

width = 8.5
height = 11

perimeter = 2 * (width + height)
diagonal = math.sqrt(width ** 2 + height ** 2)

print(f"perimeter: {perimeter:.2f}")
print(f"diagonal: {diagonal:.2f}")
