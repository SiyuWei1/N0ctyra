from main import level_text

print("Please use the followint scale:")
print(" 1. TOtally satisfied")
print(" 2.Satisfied")
print(" 3.Dissatisfied")

satisfied = int(input("What was your level of satisfaction?"))
bill = float(input("What was your bill?"))

if satisfied == 1:
    level_text = "totally satisfied"
    tip_rate = 0.20
elif satisfied == 2:
    level_text = "satisfied"
    tip_rate = 0.15
else:
    level_text = "dissatisfied"
    tip_rate = 0.15

amount = bill * tip_rate
print(f"Beacause you were {level_text} the tip amount is ${amount}.")