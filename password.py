# password.py - username and password is stored in a file.
# User must type in correct username and password to succeed!

password_file = open("passwords.txt")

username = input("Username? ")
password = input("Password? ")

for line in password_file:
    line = line.strip()
    u, p = line.split(",")  # puts the first part in variable u, and the second part in p, separated by a comma
    if u == username and p == password:
        print("Login succeeded!")
        break
else:
    print("Login failed!")

password_file.close()
