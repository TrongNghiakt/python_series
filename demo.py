age = 22
height = 168.1
name = "Nguyen Trong Nghia"
is_student = True
no_value = None

variables = [age, height, name, is_student, no_value]
for variable in variables:
    print("Value:", variable)
    print("Data type:", type(variable).__name__)
    print("Length:", len(variable) if hasattr(variable, "__len__") else "N/A")
    print()
# age = 18
# height = 1.75
# name = "Alex"
# is_student = True
# something = None

# variables = [age, height, name, is_student, something]

# for variable in variables:
#     print("Value:", variable)
#     print("Data type:", type(variable).__name__)
#     print("Length:", len(variable) if hasattr(variable, "__len__") else "N/A")
#     print()
