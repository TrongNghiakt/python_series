# Copying
# letters = ['a', 'b', 'c']
# letters_copy = letters.copy()
# letters.pop()
# letters_copy.append('z')
# print("Original list:", letters)
# print("Copied list:", letters_copy)

# import copy

# matrix = [
#     ['a', 'b'],
#     ['c', 'd']
# ]
# matrix_copy = copy.deepcopy(matrix)
# matrix.pop()
# matrix_copy[0].append('z')
# print('Original matrix:', matrix)
# print('Copied matrix:  ', matrix_copy)


import copy
original = [
    ['a', 'b'],
    ['c', 'd']
]

# Assignment
copy1 = original
print("Same Object?", original is copy1, "\n")

# Shallow Copy
copy2 = original.copy()
print("Same Object?", original is copy2, "\n")
print("Shared Lists?", original[0] is copy2[0], "\n")


# Deep Copy
copy3 = copy.deepcopy(original)
print("Same Object?", original is copy3, "\n")
print("Shared Lists?", original[0] is copy3[0], "\n")
