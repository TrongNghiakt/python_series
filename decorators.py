# Decorators - Dynamically Alter The Functionality Of Your Functions

# def outer_function(msg):
#     def inner_function():
#         print(msg)
#     return inner_function


# hi_func = outer_function("Hello")
# bye_func = outer_function("Goodbye")

# hi_func()
# bye_func()


# def decorator_function(original_function):
#     def wrapper_function(*args, **kwargs):
#         print('wrapper executed this before {}'.format(
#             original_function.__name__))
#         return original_function(*args, **kwargs)
#     return wrapper_function


# @decorator_function
# def display():
#     print("Display function ran")

# decorated_display = decorator_function(display) == @decorator_function
# display()

# class decorator_class(object):
#     def __init__(self, original_function):
#         self.orginal_function = original_function

#     def __call__(self, *args, **kwargs):
#         print('call method executed this before {}'.format(
#             self.orginal_function.__name__))
#         return self.orginal_function(*args, **kwargs)


# @decorator_function
# def display_info(name, age):
#     print("display_info ran with arguments ({}, {})".format(name, age))


# display_info("John", 25)
# display()

from functools import wraps
import time


def my_logger(orig_func):
    import logging
    logging.basicConfig(filename='{}.log'.format(
        orig_func.__name__), level=logging.INFO)

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        logging.info(
            'Ran with args: {}, and kwargs: {}'.format(args, kwargs))
        return orig_func(*args, **kwargs)
    return wrapper


def my_timer(orig_func):
    import time

    @wraps(orig_func)
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = orig_func(*args, **kwargs)
        t2 = time.time() - t1
        print('{} ran in: {} sec'.format(orig_func.__name__, t2))
        return result
    return wrapper


@my_logger
@my_timer
def display_info(name, age):
    time.sleep(1)
    print("display_info ran with arguments ({}, {})".format(name, age))


display_info("Tom", 30)
