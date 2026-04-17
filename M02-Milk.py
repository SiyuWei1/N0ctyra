# Convert the following pseudocode into Python:
# Prompt for the number of ounces of milk
# Compute the number of omelettes that can be made (4 ounces of milk per omelette)
# Use modulus division to determine the ounces of milk remaining
# Output the total number of omelettes that can be made
# Output the number of ounces remaining

milk_ounces = int(input("Please enter the number of ounces of milk: "))
omelettes = milk_ounces // 4
remaining_milk = milk_ounces % 4
print("Number of omelettes that can be made:", omelettes)
print("Ounces of milk remaining:", remaining_milk)
