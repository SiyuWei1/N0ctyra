##1
# Use a for loop to sum the even numbers from 2 to 100 (inclusive).

even_sum = 0
for num in range(2, 101, 2):
    even_sum += num
print(f"The sum of even numbers from 2 to 100 is {even_sum}")

##2
# Compute the sum of squares from 1 to 100 (inclusive).

sum_squares = 0
for i in range(1,101):
    sum_squares += i**2
print(f"The sum of squares from 1 to 100 is {sum_squares}")

##3
# Compute and print all powers of 2 from 2 ** 0 to 2 ** 20 (inclusive).
#

print("Compute and print all powers of 2 from 2 ** 0 to 2 ** 20 (inclusive)")
for i in range(21):
    print(f"2^{i} = {2 ** i}")


##4
# Prompt the user to enter integers "start" and "stop", where start < stop.
# Use a for loop to find the sum of odd numbers from start to stop (inclusive)

start = int(input("Enter a value for start: "))
stop = int(input("Enter a value for stop: "))
odd_sum = 0
for i in range(start, stop + 1):
    if i % 2 != 0:
        odd_sum += i
print(f"The sum of odd numbers from {start} to {stop} is {odd_sum}")

##5
# Prompt the user for an integer n. Then compute the factorial of n. For example, if n is 5
# n factorial = 5! = 5 * 4 * 3 * 2 * 1 = 120.

n = int(input("Enter an integer: "))
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"The factorial of {n} is {factorial}")

##6
# Compute the sum of the odd digits in an integer. Hint: refer to zyBooks section 4.15: Processing Strings.
#

num_str = input("Enter an integer: ")
odd_digit_sum = 0
for char in num_str:
    digit = int(char)
    if digit % 2 != 0:
        odd_digit_sum += digit
print(f"The sum of the odd digits in {num_str} is {odd_digit_sum}")
