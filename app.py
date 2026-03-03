def sanitize_input(user_input: str) -> str:
    """
    Remove leading and trailing whitespace from user input.
    """
    return user_input.strip()


def validate_username(username: str) -> bool:
    """
    Validate the username against allowed credentials.
    """
    return username == "seeya"


def login():
    raw_username = input("Enter username: ")
    username = sanitize_input(raw_username)

    if validate_username(username):
        print("Welcome!")
    else:
        print("Invalid username")


if __name__ == "__main__":
    login()
