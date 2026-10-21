# letters = ['a', 'b', 'c']
# # letters.append('d')
# letters.insert(0, 'x')
# letters.insert(3, 3)
# print(letters)


# Adding

# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
# # matrix.insert(0, ['x', 'y', 'z'])
# matrix[1].append('x')
# matrix[0].insert(0, 'y')
# print(matrix)


# Removing
# letters = ['a', 'b', 'c']
# # letters.clear()
# # letters.remove('a')
# removed = letters.pop(1)
# print(letters)
# print(removed)


# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i']
# ]
# matrix[1].remove('e')
# matrix[-1].pop(0)
# matrix[0].pop()
# print(matrix)


# Updating
# letters = ['a', 'b', 'c']
# letters[0] = 'x'
# letters = 'z'
# print(letters)


matrix = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
]
matrix[2] = ['x', 'y', 'z']
matrix[0][0] = 'x'
matrix[1][1] = 'y'
matrix[-1][-1] = '-'
print(matrix)
