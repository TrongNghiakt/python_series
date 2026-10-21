
# start = int(input("Enter your score: "))
# submitted_project = False

# if start >= 90:
#     print("Hight score! You got an A.")
# else:
#     print("You did not get an A. Keep trying!")

# if submitted_project:
#     print("You submitted your project. Good job!")
# else:
#     print("You did not submit your project. Please submit it as soon as possible.")

email = "23432"
password = "a23432#"
valid = True
if password == "":
    print("Password cannot be empty")
    valid = False
if len(password) < 8:
    print("Password must be at least 8 characters long")
    valid = False
if not any(char.isupper() for char in password):
    print("Password must contain at least one uppercase letter")
    valid = False
if not any(char.islower() for char in password):
    print("Password must contain at least one lowercase letter")
    valid = False
if password == email:
    print("Password cannot be the same as the email")
    valid = False
if " " in password:
    print("Password cannot contain leading or trailing spaces")
    valid = False
if password:
    if not (password[0].isdigit() or password[0].isalpha()):
        print("Password must start with a letter or a digit")
        valid = False
    if not (password[-1].isdigit() or password[-1].isalpha()):
        print("Password must end with a letter or a digit")
        valid = False
if valid:
    print("Password is valid")
