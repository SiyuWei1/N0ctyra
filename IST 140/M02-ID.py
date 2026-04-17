# Write a program to create an ID for a student by taking the first letter of their first name and adding the last 4 digits of their phone number to it.
# Prompt for their name. Prompt for their phone number.

name = input('Enter your first name: ')
phone_number = input('Enter your phone number (digits only): ')
first_letter = name[0]
last_four = phone_number[-4:]
ID = first_letter + last_four
print("Your student ID is: " + ID)
