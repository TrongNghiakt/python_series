# Transformations

# first_name = "Nghia"
# last_name = "Nguyen"
# print(first_name + " " + last_name)

# folder = "C:/Users/Nghia"
# file = "report.csv"
# full_file_path = folder + "/" + file
# print(full_file_path)


# f-Strings
# name = "Nghia"
# age = 22
# is_student = False
# print("My name is " + name, "I am " + str(age),
#       "years old, and student status is " + str(is_student))

# print(
#     f"My name is {name}, I am {age} years old, and student status is {is_student}")

# print(f"2 + 3 = {2 + 3}")

# print(f"{{This is me}}")


# split() method
# stamp = "2026-90-20"
# print(stamp.split("-"))

# csv_file = "1234,Max,USA,1970-10-05,M"
# print(csv_file.split(","))


# print("ha"*3)


# Indexes & Slicing
# text = "Python"

# # Extract the first character
# print(text[0])  # Output: P
# print(text[-6])

# # Extract the last character
# print(text[-1])  # Output: n
# print(text[5])   # Output: n

# # Extract h
# print(text[3])
# print(text[-3])


# date = "2026-09-20"
# print(date[0:4])  # Output: 2026
# print(date[5:7])  # Output: 09
# print(date[8:])  # Output: 20
# print(date[-2:])


# Whitespace Cleanup
# text = " Engineering".lstrip()  # Remove leading whitespace
# print(text)  # Output: "Engineering"

# text = "Engineering ".rstrip()
# print(text)  # Output: "Engineering"

# text = "  Engineering       ".strip()  # Remove leading and trailing whitespace
# print(text)  # Output: "Engineering"


# text = "Data Engineering".strip()
# print(text)


# text = "####Abc##".strip("#")
# print(text)  # Output: "Abc"


# text = "Data Engineering"

# nr_of_spaces = len(text) - len(text.strip())
# is_clean = len(text) == len(text.strip())

# print("Number of spaces:", nr_of_spaces)
# print("Is clean:", is_clean)


# Case Conversion
# text = "python PROGRAMMING"
# print(text.lower())
# print(text.upper())

# search = "Email ".lower().strip()
# data = " emAil".lower().strip()

# print(search == data)


# text = "968-Maria, (D@t@ Engineer );; 27y.."
# name = text.split("-")[1].split(",")[0].strip().lower()
# role = text.split("(")[1].split(")")[0].strip().replace("@", "a").lower()
# age = text.split(";")[-1].strip().strip(".").strip("y")
# print(f"name: {name} | role: {role} | age: {age}")
