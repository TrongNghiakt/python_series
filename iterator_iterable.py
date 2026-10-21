# letters = ['a', 'b', 'c']
# new_list = []
# for i in letters:
#     new_list.append(i.upper())
#     print(i.upper())
# print(new_list)


# letters = ['a', 'b', 'c']
# numbers = [1, 2, 3]
# # print(list(reversed(letters)))
# # for index, value in enumerate(letters):
# #     print(f"Index: {index}, Letter: {value}")

# # for l in reversed(letters):
# #     print(l)

# # print(list(zip(letters, numbers)))
# for index, values in zip(letters, numbers):
#     print(f"Letter: {index}, Number: {values}")


# letters = ['1', '2', '3']
# print(list(map(int, letters)))

# names = [' Maria ', 'John ', ' Kumar']
# # print(list(map(str.strip, names)))
# for n in map(str.strip, names):
#     print(n)


letters = ['a', '', 'b', 'c', 0, None, True, False, 2]
print(list(filter(bool, letters)))

items = ['sql', '123', 'python', '456']
print(list(filter(str.isalpha, items)))
