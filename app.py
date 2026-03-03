def login():
    username = input("Enter username: ")
    
    if username == "seeya":
        print("Welcome!")
    else:
        print("Invalid username")

if __name__ == "__main__":
    login()
