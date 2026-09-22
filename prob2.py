import re


def check_username(username):

    min_length = 5
    max_length = 15

    if not (min_length <= len(username) <= max_length):
        return f"Invalid: Length must be between {min_length} and {max_length} characters."


    if not username[0].isalpha():
        return "Invalid: First character must be a letter."


    if not re.match("^[a-zA-Z0-9_]*$", username):
        return "Invalid: Only letters, and numbers are allowed."

    return "Valid username!"



user_input = input("Enter a username: ")
print(check_username(user_input))
