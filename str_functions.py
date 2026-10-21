# Built-in functions
# name = "Nghia"
# print(type(name))

# age = 22
# print(type(age))
# print("Your Age is " + str(age))
# print(type(age))

# age = str(age)
# print(type(age))


# Math
# password = "  123adasfas234"
# print(len(password))
# if len(password) < 8:
#     print("Password is too short")


# text = """
# Python is easy to learn.
# Python is powerful.
# Many pepole use Python for data science, web development, and more.
# """

# print(text.count("python"))


# Transformations
# price = "1234,56"
# print(price.replace(",", "."))

# price = "$1,299.99"
# print(price.replace("$", "").replace(",", ""))

phone = "+49 (176) 123-4567"
print(phone.replace("+", "00").replace("(", "").replace(" ",
      "").replace(")", "").replace("-", ""))
