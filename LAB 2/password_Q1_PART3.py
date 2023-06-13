prev_pass = "abc$123"

username = input("Enter your username: ")
password = input("What is the password? ")

if password.lower() == prev_pass.lower():
    print("Welcome!")
else:
    print("I don't know you.")