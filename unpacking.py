# person = 'Hi'
# # name = person[0]
# # age = person[1]
# # job = person[2]
# # country = person[3]

# name, *rest = person
# print(name, rest)


# person = ['Maria', 29, 'Data Engineer', 'USA']
# name, _, role, _ = person
# print(name, role)


lists = [30, 40, 45, 30, 1, 22, 15, 5]
first, *_, middle, last = lists
print(first, middle, last)
