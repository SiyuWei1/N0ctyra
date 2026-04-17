temp = float(input("Enter the temperature value: "))
unit = input("Enter the C for Celsius or F for Fahrenheit: ")
if unit == "C":
    if temp > 100:
        print("Water is gas.")
    elif temp > 0:
        print("Water is liquid.")
    else:
        print("Water is solid.")
elif unit == "F":
    if temp > 212:
        print("Water is gas.")
    elif temp > 32:
        print("Water is liquid.")
    else:
        print("Water is solid.")
