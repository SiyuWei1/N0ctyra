month = int(input("Please enter the month as a number 1-12: "))
day = int(input("Please enter the day of the month as number 1-31: "))

if month == 1 or month == 2 or month == 3:
    season = "Winter"
elif month == 4 or month == 5 or month == 6:
    season = "Spring"
elif month == 7 or month == 8 or month == 9:
    season = "Summer"
else:
    season = "Fall"

if month % 3 == 0 and day >= 21:
    if season == "Winter":
        season = "Spring"
    elif season == "Spring":
        season = "Summer"
    elif season == "Summer":
        season = "Fall"
    else:
        season = "Winter"

print(season)