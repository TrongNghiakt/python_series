# # Combining
# letters = ['a', 'b', 'c', 4]
# numbers = [1, 2, 3]
# # comb = [letters, numbers]
# # print(comb)
# # print(letters * 2)
# # print(numbers * 2)

# # numbers.extend(letters)
# # print(numbers)


# comb = zip(letters, numbers, "hi")
# print(list(comb))


ids = [101, 102, 103]
names = ['Ali', 'Sara', 'John']
comb = zip(ids, names)
print(ids + names)
print(list(comb))
