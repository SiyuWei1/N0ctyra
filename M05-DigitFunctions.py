def firstDigit(n): # returns the first digit of the argument
    while n >= 10:
        n = n // 10
    return n

def lastDigit(n): # returns the last digit of the argument
    return n % 10

def digits(n): # returns the number of digits in the argument
    count = 0
    while n > 0:
        n = n // 10
        count = count + 1
    return count

print("firstDigit of 1855 is", firstDigit(1855))
print("firstDigit of 2099 is", firstDigit(2099))
print("firstDigit of 987 is", firstDigit(987))

print("lastDigit of 1855 is", lastDigit(1855))
print("lastDigit of 2099 is", lastDigit(2099))
print("lastDigit of 987 is", lastDigit(987))

print("digits of 1855 is", digits(1855))
print("digits of 2099 is", digits(2099))
print("digits of 987 is", digits(987))
