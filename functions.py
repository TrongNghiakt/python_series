# text = "Hi"
# number = 10


# # Built-in functions
# print(type(text))
# print(type(number))

# print(len(text))
# print(len(str(number)))


# # Method of class
# print(text.upper())
# # print(number.upper())
# # print(str(number).upper())


# print(number.bit_length())
# # This will raise an AttributeError since 'str' object has no attribute 'bit_length'
# print(text.bit_length())


# # Enumerate function
# my_list = [100, 200, 300, 400, 500]
# for i, x in enumerate(my_list):
#     print(x)


# Pass keyword
# def hello_func():
#     pass


# print(hello_func())  # Output: None


# Executing function
# def hello_func():
#     return "Hello Function!"


# hello_func()
# print(hello_func())  # Output: Hello Function!


# def hello_func(greeting, name="You"):
#     return "{}, {}".format(greeting, name)
# print(hello_func("Hi", "kaka"))


# Positional keyword arguments
# def student_info(*args, **kwargs):
#     print(args)
#     print(kwargs)


# course = ['Math', 'Art']
# info = {'name': 'John', 'age': 22}
# # Output: (['Math', 'Art'], {'name': 'John', 'age': 22})
# student_info(*course, **info)


# Example
# Number of days per month. First value placeholder for indexing purposes.
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True of leap year, False for non-leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):
    """Return nubmer of days in that month in that year."""

    if not 1 <= month <= 12:
        return "Invalid Month"
    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(days_in_month(2020, 2))  # Output: 29
