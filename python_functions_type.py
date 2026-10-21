# 1.Action funtions
# Task: store application log messages in a file
# def write_log(message):
#     with open(r"D:\python_learning\app.log", "a") as file:
#         file.write(message + "\n")


# # write_log("Application started")
# # write_log("User logged in")
# write_log("App stopped")


# 2. Transfomation functions
# Task: clean an email and split it into username and domain
# def clean_and_split_email(email):
#     cleaned_email = email.strip().lower()
#     username, domain = cleaned_email.split("@")
#     return {"username": username, "domain": domain}


# print(clean_and_split_email("    SARA@gmAil.com  "))


# 3. Validation funtions
# Task: Check if a passwor meets the minium length of 8
# def is_valid_password(password):
#     return len(password) >= 8


# print(is_valid_password("password123"))  # True


# Task: Check if email has a basic valid format
# def is_valid_email(email):
#     return "@" in email and "." in email.split("@")[-1]


# print(is_valid_email("@saragmail.com"))


# 4. Orchestrator functions
# Task: Build small project
# We receive an email from a user
# We must check if it is valid
# If it is not valid, we log the problem
# If it is valid, we clean it and store structured information
# And we log what happened
def write_log(message):
    with open(r"D:\python_learning\app.log", "a") as file:
        file.write(message + "\n")


def is_valid_email(email):
    return "@" in email and "." in email.split("@")[-1]


def clean_and_split_email(email):
    cleaned_email = email.strip().lower()
    username, domain = cleaned_email.split("@")
    return {"username": username, "domain": domain}


# Orchestrator function
def process_user_email(email):
    write_log("Application started")
    if not is_valid_email(email):
        write_log(f"Invalid email received: {email}")
    else:
        clean_email = clean_and_split_email(email)
        write_log(f"Processed Email: {clean_email}")

    write_log("Application stopped")


email = input("Please enter your email: ")
process_user_email(email)
