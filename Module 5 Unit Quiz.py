# Write a Python program that uses the code provided in the main menu loop to drive the program.
# Do NOT change this code. Make sure to submit ALL of your code when you are done.

# Code the following functions using the pseudocode to guide you:
# **Library System Pseudocode**

#
# **Function: get_user_info()**
# - Prompt the user for their first name
# - Prompt the user for their last name
# - Prompt the user for their favorite book genre
# - Call create_user_id and pass first name, last name, and favorite genre as arguments
#
def get_user_info():
    first_name = input("First name: ")
    last_name = input("Last name: ")
    fav_genre = input("Favorite genre: ")
    create_user_id(first_name, last_name, fav_genre)


# **Function: create_user_id(first_name, last_name, fav_genre)**
# - Take the first letter of the first name (lowercase)
# - Add the full last name (lowercase)
# - Add the first three letters of the genre (lowercase)
# - Add the number "123"
# - Combine all parts into a user ID
# - Call print_user_id and pass the user ID
#
def create_user_id(first_name, last_name, fav_genre):
    user_id = first_name[0].lower() + last_name.lower() + fav_genre[:3].lower() + "123"
    print_user_id(user_id)

# **Function: print_user_id(user_id)**
# - Print: "Your new library user ID is:" followed by the user ID
#
def print_user_id(user_id):
    print("Your new library user ID is: ", user_id)

# **Function: get_book_info()**
# - Prompt the user for the title of a book
# - Prompt the user for the author of the book
# - Prompt the user for the due date of the book
# - Call print_book_info and pass title, author, and due date
#
def get_book_info():
    title = input("Book title: ")
    author = input("Book author: ")
    due_date = input("Book due date: ")
    print_book_info(title, author, due_date)

# **Function: print_book_info(title, author, due_date)**
# - Print: "You checked out:" followed by the book title, author, and due date
#
def print_book_info(title, author, due_date):
    print("You checked out", title, "by",author)
    print("It is due on", due_date)

# Main Menu Loop - DO NOT EDIT THIS CODE
def main():
    keep_running = True
    while keep_running:
        print("\n--- Library System ---")
        print("1. Create User ID")
        print("2. Check Out a Book")
        print("3. Exit")
        option = input("Choose an option (1-3): ")

        if option == "1":
            get_user_info()
        elif option == "2":
            get_book_info()
        elif option == "3":
            print("Thank you for using the Library System!")
            keep_running = False
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


main()