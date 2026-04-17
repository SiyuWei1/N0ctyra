# 1. A student has completed 4 quizzes with scores of 75, 88, 90, and 82.
# The professor allows them to drop their lowest score and replace it with a new score.
# Write a Python program that:

# Assign each score to a variable.
# Ask the student to enter a new score.
# Drop the lowest score from the original 4 scores. Hint: Use the min() function.
# Replace the lowest score with the new score.
# Calculate and display the new average score.

# WRITE YOUR CODE FOR QUESTION 1 HERE

scores1 = 75
scores2 = 88
scores3 = 90
scores4 = 82

new_scores = float(input("Enter a new score: "))
scores = [scores1, scores2, scores3, scores4]
min_scores = min(scores)
scores.remove(min_scores)
scores.append(new_scores)
avarage = sum(scores) / len(scores)
print("New average score is:", avarage)

# 2. Write a Python program that:

# Prompts the user to enter a sentence.
# Calculates and displays the length of the sentence. Hint: Use the len() function.
# Displays the first 3 letters of the sentence and the last 3 letters of the sentence.

# WRITE YOUR CODE FOR QUESTION 2 HERE
sentence = input("\nEnter a sentence: ")

length = len(sentence)
print("Sentence length: ", length)
print("First three letters:", sentence[:3])
print("Last three letters:", sentence[-3:])

# 3. A bookstore offers a 10% discount if a customer buys 4 books. Write a Python program that:

# Prompts the user to enter the price of 4 books (one at a time, as floats).
# Calculates the total cost of the books.
# Applies a 10% discount to the total cost.
# Displays the total amount owed, with two decimal places of precision.

# WRITE YOUR CODE FOR QUESTION 3 HERE

print("\nEnter the prices of 4 books:")

book1 = float(input("Book 1 price: "))
book2 = float(input("Book 2 price: "))
book3 = float(input("Book 3 price: "))
book4 = float(input("Book 4 price: "))

total_cost = book1 + book2 + book3 + book4
discounted_total = total_cost * 0.90
print("Total amount owed: {:.2f}".format(discounted_total))
