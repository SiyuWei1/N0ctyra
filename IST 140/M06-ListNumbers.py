# Read 10 floating-point numbers from the user, adding each to a list if it is not already present.
# Once the list is complete (i.e., contains 10 unique floating-point numbers), print the numbers
# in the order in which the user entered them.

numbers = []

while len(numbers) < 10:
    points = float(input("Enter a number: "))
    if points not in numbers:
        numbers.append(points)

for num in numbers:
    print(num)