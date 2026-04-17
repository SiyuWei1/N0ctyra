# Write a program that reads in three floating-point numbers and prints the largest of the three inputs without using the max function.

num1 = float(input("Enter a number:"))
num2 = float(input("Enter a number:"))
num3 = float(input("Enter a number:"))
final_num = 0

if num1 > num2:
    final_num = num1
else:
    final_num = num2

if num3 > final_num:
    final_num = num3

print("The largest number is", final_num)