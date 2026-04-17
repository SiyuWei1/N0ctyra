

# Generate a list of 10 random numbers between 1 and 100 (see zyBooks 4.16 for a refresher on random numbers). Then:
# 1. Print the list of numbers all on one line, separated with spaces
# 2. Print the elements at even indices all on one line, separated with spaces
# 3. Print the even elements all on one line, separated with spaces
# 4. Print the elements in reverse order, all on one line, separated with spaces
# 5. Display the first and last element

import random

nums = [random.randint(1, 100) for _ in range(10)]

print("1.", *nums)
print("2.", *[nums[i] for i in range(0, 10, 2)])
print("3.", *[x for x in nums if x % 2 == 0])
print("4.", *nums[::-1])
print("5.", nums[0], nums[-1])

