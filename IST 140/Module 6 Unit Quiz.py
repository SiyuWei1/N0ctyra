# Write a Python program that uses the code provided in the main() function to drive the program.
# Do NOT change the code in main().
# Copy all of these comments and provided code to PyCharm
# Make sure to submit ALL of your code when you are done.

# Scenario: You are writing a script to track contestant performance on a comedy game show.
# You will see four functions to implement; the first one is self-contained.
# Code the following functions using the pseudocode to guide you:

# 1. get_task_times()
#     This function doesn't relate to the other functions; it's self-contained.
#     This function prompts for 5 task completion times (in seconds) to fill a list with integers.
#     You do not need to validate that the time is in any particular range.
#     Find the average of the times *with the highest (slowest) one dropped*.
#     Print the average to the console, to two decimals of precision.
#     This function is called from main, takes no parameters, and returns nothing.

def get_task_times():
    times = []
    for i in range(5):
        t = int(input("Enter a task completion time (in seconds): "))
        times.append(t)

    slowest = times[0]
    for t in times:
        if t > slowest:
            slowest = t
    times.remove(slowest)

    total = 0
    for t in times:
        total += t

    average = total / len(times)
    print(f"Average time with the slowest attempt dropped is: {average:.2f}")


# 2. get_contestant_name()
#     This function takes no parameters and returns a string.
#     Request a string from the user to be used for the contestant's name.

def get_contestant_name():
    name = input("Enter the contestant's name: ")
    return name

# 3. get_task_scores()
#     This function takes no parameters and returns a list of integers 1 to 5 (inclusive).
#     Ask the user to enter a list of scores awarded for different tasks, and to enter "Finish" when done.
#     Do not allow them to enter anything outside the bounds of 1 to 5; print an error message like in the Sample Run below.
#     The function returns these numbers in the list.

def get_task_scores():
    scores = []
    entry = input("Enter a score between 1 and 5; enter Finish to stop: ")
    while entry != "Finish":
        value = int(entry)
        if value > 0 and value < 6:
            scores.append(value)
        else:
            print("ERROR: Score must be between 1 and 5")
        entry = input("Enter a score between 1 and 5; enter Finish to stop: ")
    return scores

# 4. print_score_board(name, scores)
#     This function takes a string (the contestant name) and a list of integers as parameters.
#     Print the contestant's name and a histogram using the list of integers as data.
#     Each value in the list is the number of hash symbols (a hash and then a space) to print on that line.
#     Each element in the list is a separate line in the graph representing a task score.

def print_score_board(name, scores):
    print()
    print("Contestant:", name)
    for score in scores:
        print("# " * score)


def main():
    get_task_times()
    contestant = get_contestant_name()
    points = get_task_scores()
    print_score_board(contestant, points)

main()