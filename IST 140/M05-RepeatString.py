def repeat(string, n, delim):
    return delim.join([string] * n)


string = input("Enter a string: ")
n = int(input("Enter a number of times to repeat: "))
delim = input("Enter a delimiter: ")

print(repeat(string, n, delim))


