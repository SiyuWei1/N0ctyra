

##1
# Prompt the user for an integer, n.
# Then use a nested for loop to print a multiplication table from 1 to n.
# You may wish to refer to zyBooks Table 2.12.1: Format Specifier Examples
# for ideas on how to make the numbers in the table line up nicely.

# WRITE YOUR CODE FOR QUESTION 1 HERE
n1 = int(input("Enter an integer: "))

for row in range(1, n1 + 1):
    for col in range(1, n1 + 1):
        print(f"{row * col:3}", end=" ")
    print()

print()

##2
# Prompt the user for an integer, n.
# Use a nested for loop to print an n x n grid where the diagonal
# shows 1 and others show 0.

# WRITE YOUR CODE FOR QUESTION 2 HERE
n2 = int(input("Enter an integer: "))

for i in range(n2):
    for j in range(n2):
        if i == j:
            print(f"{1:3}", end=" ")
        else:
            print(f"{0:3}", end=" ")
    print()