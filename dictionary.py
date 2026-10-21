# my_dict = {
#     'a': 10,
#     'b': 20,
#     'c': 30,
#     'd': 10
# }

# print(my_dict)  # Ordered
# # Keys are Unique
# # Values allow Duplicates

# print(my_dict['a'])  # Not Indexed (Keyed)

# my_dict['c'] = 100
# print(my_dict)  # Mutable (Insert, Update, Delete)


# user = {"id": 1, "age": 30, "city": "berlin"}

# Access
# print(user["id"])
# print(user.get("name", "Unknown"))

# # Checks
# print("age" in user)
# print("name" not in user)

# # View Objects
# print(user.keys())
# print(user.values())
# print(user.items())
# print(user)

# Looping
# for key, value in user.items():
#     print(key, value)


# # Add, Remove, Update
# user["name"] = "John"  # Add
# user["age"] = 23      # Update
# user.update({"age": 40, "city": "London"})  # Update
# print(user)

# age = user.pop("salary", "Not Found")  # Remove
# print(user)
# print("Remove Item:", age)

# user.popitem()
# print(user)


# Creation
# user = {"id": None, "name": None, "age": None, "city": None}

# users = dict.fromkeys(["id", "name", "age", "city"], None)
# print(user, "\n", users)

# user["age"] = 40
# print(user)


# Challange: Keep only string values & Convert them to uppercase
user = {"id": 1, "name": "Johna", "age": 30, "city": "Berlin"}

user_str = {
    # Expression
    # Loop
    # Filter
    k: v.upper()
    for k, v in user.items()
    if isinstance(v, str)
}
print(user_str)
