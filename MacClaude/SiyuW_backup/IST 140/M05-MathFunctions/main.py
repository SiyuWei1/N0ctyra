def smallest(x, y, z):
    if x <= y and x <= z:
        return x
    elif y <= x and y <= z:
        return y
    else:
        return z

def average(x, y, z):
    return (x + y + z) / 3

print("The smallest number of 7, 9, and 8 is", smallest(7, 9, 8))
print("The average of 1984, 2013, and 2015 is", average(1984, 2013, 2015))
