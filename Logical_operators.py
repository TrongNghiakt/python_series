user_name = input("Enter your name: ")
age = int(input("Enter your age: "))
password = input("Enter your password: ")
email = input("Enter your email: ")
role = input("Enter your role (admin/moderator/user): ")
is_banned = input("Is the user banned? (yes/no): ").lower()


if user_name != "" and age >= 18:
    print("Access granted")
else:
    print("Name must not be empty and age must be at least 18")

if len(password) >= 8 and password.find(" ") == -1:
    print("Password is valid")
else:
    print("Password must be at least 8 characters long and cannot contain spaces")

if email != "" and email.find("@") != -1 and email.endswith(".com") == True:
    print("Email is valid")
else:
    print("Email must cointain '@' and end with '.com'")

if isinstance(user_name, str) and user_name is not None and len(user_name) >= 5:
    print("Username is valid")
else:
    print("Username must be a string and longer than 5 characters")

if (role == "admin" or role == "moderator") and (not is_banned or is_verified):
    print("User has access")
else:
    print("User does not have access")
