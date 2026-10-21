# # # Unorderd Collection of Unique Values
# # my_set = {10, 30, 20, 10}
# # print(my_set)       # Unordered # Unique
# # # print(my_set[1])    # Not indexed

# # my_set.remove(30)
# # print(my_set)       # Mutable (Insert, Update, Delete)


# a = {10, 20, 30, 40}
# a.add(50)

# # a.update({1, 2})
# a |= {1, 2}
# # a.pop()

# # a.remove(100)

# a.discard(20)  # No Error
# print(a)


# a = {10, 20, 30, 40}
# b = {30, 40, 50, 60}
# Mathematical Operations
# print(a.union(b))  # a | b
# # print(a | b)  # a | b

# print(a.intersection(b))  # a & b
# print(a & b)

# print(a.difference(b))  # a - b
# print(b-a)

# print(a.symmetric_difference(b))  # a ^ b
# print(a ^ b)

a = {31, 41}
b = {30, 40, 50, 60}
print(a.issubset(b))
print(b.issuperset(a))

print(a.isdisjoint(b))
