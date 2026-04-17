# 1. Write a Python snippet that prompts the user to enter a greeting.
# If the user enters "Hello", output "Hi there!".
# If the user enters "Goodbye", output "See you later!".
# For any other input, output "I don't understand."

# WRITE YOUR ANSWER TO QUESTION 1 HERE
str = input("Enters a greeting: ")
if str == "Hello":
    print("Hi there!")
elif str == "Goodbye":
    print("See you later!")
else:
    print("I don't understand.")


# 2. Write a Python snippet that asks the user to choose between "Breakfast", "Lunch", or "Dinner".
# If the user enters an invalid choice, output "Invalid entry." and do nothing else.
# If the user enters a valid choice, ask them to enter a drink: "Coffee", "Juice", or "Water".
# If the drink is valid, output a response based on their meal and drink combination:
# "Breakfast with Coffee is a great start!"
# "Lunch with Juice is refreshing!"
# "Dinner with Water is a healthy choice!"
# If an invalid drink is entered, output "Invalid drink choice."

# Sample Runs:
# Valid Input:
# Enter a meal: Lunch
# Enter a drink: Juice
# Lunch with Juice is refreshing!
#
# Invalid Meal:
# Enter a meal: Snack
#
# Invalid entry.
#
# Valid Meal but Invalid Drink:
# Enter a meal: Dinner
# Enter a drink: Soda
# Invalid drink choice.

# WRITE YOUR ANSWER TO QUESTION 2 HERE
meal = input("Make a choice bewteen 'Breakfast', 'Lunch' or 'Dinner': ")
if meal != "Breakfast" or meal != "Lunch" or meal != "Dinner":
    print("Invalid entry.")
else:
    drink = input("Enter a drink bewteen 'Coffee', 'Juice' or 'Water': ")
    if drink != "Coffee" or drink != "Juice" or drink != "Water":
        print("Invalid drink choice.")
    else:
        if meal == "Breakfast" and drink == "Coffee":
            print("Breakfast with Coffee is a great start!")
        elif meal == "Lunch" and drink == "Juice":
            print("Lunch with Juice is refreshing!")
        elif meal == "Dinner" and drink == "Water":
            print("Dinner with Water is a healthy choice!")

# 3. Understanding Boolean Logic
# For the following code, what is the correct output? Explain your reasoning.
# condition = (50 < 40) or (75 == 75) and (200 > 300)
# if condition == True:
#     print("Success!")
# else:
#     print("Failure!")

# WRITE YOUR ANSWER TO QUESTION 3 HERE (AS A COMMENT)

# condition = (50 < 40) or (75 == 75) and (200 > 300)
# (50 < 40) is False
# (75 == 75) is True
# (200 > 300) is False
# 'and' is evaluated before 'or'
# so (75 == 75) and (200 > 300) is True and False -> False
# then (50 < 40) or Flase -> False or False -> Flase
# It will print
# Failure!