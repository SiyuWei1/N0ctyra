# 1. Write a Python code snippet that prints your name and your favorite thing about winter.
# Each piece of information should be on a separate line.

# WRITE YOUR ANSWER HERE
print("Siyu Wei")
print("My favorite thing about winter is the quiet feeling of after snows.")

# 2. Using Python, output an email to your professor asking for guidance on places to get additional Python practice. You may use the example below directly, or you may write your own. It would be nice, but not required, to include blank lines, as in the example. Include a salutation, three sentences in the body, and a polite closing.

# Example:
# Hi Marc,
#
# I hope this email finds you well. I love Python and would love to get even more practice, beyond what's in zyBooks. Could you point me to any additional resources?
#
# Sincerely,
# [Your Name]

# WRITE YOUR ANSWER HERE
print("Hi Professor,")
print()
print("I hope you are doing well.")
print("i have been enjoying learning Python in class and would to get more practice beyond the assigned work.")
print("Could you please recommend any website or resources where I can improve my skill?")
print()
print("Sincerely,")
print("Siyu Wei")

# 3. A delivery van has a maximum capacity of 1,000 kilograms. It is currently carrying 4 large crates, each weighing 100 kilograms.
# Write a Python snippet to calculate the remaining weight capacity of the van. Have Python do the math for you.
# Output should be in this format:
# "The van can still hold ___ kilograms."

# WRITE YOUR ANSWER HERE
max = 1000
crates = 4
weight = 100
remain = max - crates * weight
print("The van can still hold", remain, "kilograms")
# 4. Consider a variation on the van problem in Question 3. Assume the van has only 300 kilograms of remaining capacity.
# Using comments, write an algorithm to check whether a crate weighing x kilograms can board the van.
# Use clear steps in your comments to outline the process.

# WRITE YOUR ANSWER HERE

# 1. Set the remaining capacity of the van to 300 kilograms.
# 2. Get the weight of the crate (x).
# 3. Compare x to the remaining capacity.
# 4. If x is less than or equal to 300, the crate can be loaded.
# 5. If x is greater than 300, the crate cannot be loaded.
# 6. Output the result.
