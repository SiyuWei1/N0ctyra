# 1. Write a Python code snippet that prints out your name and your favorite color on one line.
# print("My name is Siyu Wei, and my favorite color is red")
name = "Siyu Wei"
Color = "red"
print("My name is " + name, "My favorite color is " + Color)

# 2. The price of gas in Pennsylvania is $4 and the price of gas in New Jersey is $3.
# Write a code snippet that outputs the cost to fill a car’s tank if it has a capacity of 14 gallons.
# Output:
# The price to fill up the car in NJ is …
# The price to fill up the car in PA is …
pricePa = 4
priceNj = 3
tank = 14
costPa = pricePa * tank
costNj = priceNj * tank
print("The price to fill up the car in NJ is $", priceNj)
print("The price to fill up the car in PA is $", pricePa)

# 3. The code below may have a few errors in it.
# Fix the code below so that it matches the output and no errors remain:
# Desired Output:
# The length of a football field is 120 yards
# The width of a football field is 53 yards
# That means the perimeter of the field is 346 yard

# print("The length of the football field is 120 yards", "The length of the football field is 53 yards")
# print("That means the perimeter of the field is 346 yards")
print("The length of a football field is 120 yards")
print("The width of a football field is 53 yards")
print("That means the perimeter of the field is 346 yards")

# 4. Consider question 2. Using comments, write an algorithm that
# compares the two prices to see which is greater
# and calculates the difference between the larger and smaller.

# 1. Store the gas prices for Pennsylvania and New Jersey
# 2. Compare the two prices to determine which one is greater
# 3. Subtract the smaller price from the larger price
# 4. Store the difference
# 5. Output which state has the higher price and the price difference
if (pricePa > priceNj):
    difference = pricePa - priceNj
    print("Pennsylvania has the higher price and the price difference is $", difference)
else:
    difference = priceNj - pricePa
    print("New Jersey has the higher price and the price difference is $", difference)
