def password():
    password = input("Enter Password: ")

    if password.lower() == password:
        print("Correct Password.")
        print("Welcome to the System!")
    else:
        print("Incorrect Password.")
        print("System Closed.")