temp = float(input("Enter the temperature value: "))
unit_temp = input("Enter the C for Celsius or F for Fahrenheit: ")
altitude = float(input("Enter the altitude value: "))
unit_alt = input("Enter the M for Meters or Ft for Feet: ")

if unit_alt == "M":
    boiling_c = 100 - (altitude / 300)
elif unit_alt == "Ft":
    boiling_c = 100 - (altitude / 1000)

if unit_temp == "C":
    if temp > boiling_c:
        print("Water is gas.")
    elif temp > 0:
        print("Water is liquid.")
    else:
        print("Water is solid.")
elif unit_temp == "F":
    boiling_f = (boiling_c * 9 / 5) + 32
    if temp > boiling_f:
        print("Water is gas.")
    elif temp > 32:
        print("Water is liquid.")
    else:
        print("Water is solid.")
