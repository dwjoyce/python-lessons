# password_strength.py
# Ask user to choose a password, and as long it is valid, tell them whether
# it is a strong, medium or weak password.

valid_password = False

while not valid_password:
    password_string = input("Please enter the password: ")

    if len(password_string) < 6:
        print("Password too short!")

    elif len(password_string) > 12:
        print("Password too long!")

    else:
        lowercase = uppercase = numerical = 0

        for character in password_string:
            if character.islower():
                lowercase = 1
            elif character.isupper():
                uppercase = 1
            elif character.isdigit():
                numerical = 1

            if lowercase and uppercase and numerical:
                break

        password_strength = lowercase + uppercase + numerical

        if password_strength in [1, 2, 3]:  # or range(1, 4)
            print("Valid password!")

            if password_strength == 1:
                print("Weak password")
            elif password_strength == 2:
                print("Medium password")
            elif password_strength == 3:
                print("Strong password")

            valid_password = True
        else:
            print("Invalid Password, please try again.")
