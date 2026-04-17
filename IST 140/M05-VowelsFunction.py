def countVowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count

user_string = input("Enter a string: ")
vowel_count = countVowels(user_string)
print(f"There are {vowel_count} vowels in: {user_string}")