# Write a program that prompts the user for a string and two integers,
# then prints a slice of the string using the two integers as the starting and end positions.

string = input("Enter a string: ")
start = int(input("Enter the starting position: "))
end = int(input("Enter the ending position: "))
print("Here is the sliced string: ", string[start:end])
