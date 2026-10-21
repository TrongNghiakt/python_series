# # # Measure Distance
# # print(abs(2-10))


# # Rounding Numbers
# from math import ceil, floor, trunc


# price = 35.2354234
# print(round(price))
# print(round(price, -1))
# print(floor(price))
# print(ceil(price))
# print(trunc(price))
# print(int(price))

# import random
# # print(random.random())
# print(random.randint(1, 6))


# x = 7.3
# print(x.is_integer())

# x = 70.4
# print(isinstance(x, int))
# print(isinstance(x, float))

import random

x = random.randint(1, 100)
print("Random number:", x)
if x % 2 == 0:
    print("Even number")
else:
    print("Odd number")
