text = "Hi"
number = 10


# Built-in functions
print(type(text))
print(type(number))

print(len(text))
print(len(str(number)))


# Method of class
print(text.upper())
# print(number.upper())
# print(str(number).upper())


print(number.bit_length())
# This will raise an AttributeError since 'str' object has no attribute 'bit_length'
print(text.bit_length())
