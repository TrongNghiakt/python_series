import logging
import employee

# DEBUG: Detailed information, typically of interest only when diagnosing problems.

# INFO: Confirmation that things are working as expected.

# WARNING: An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.

# ERROR: Due to a more serious problem, the software has not been able to perform some function.

# CRITICAL: A serious error, indicating that the program itself may be unable to continue running.

# logging.basicConfig(filename='Logging-Advanced\\test.log', level=logging.DEBUG,
#                     format='%(asctime)s:%(name)s:%(message)s')

logger = logging.getLogger(__name__)

logger.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s:%(name)s:%(message)s')

file_handler = logging.FileHandler('Logging-Advanced\\sample.log')

file_handler.setLevel(logging.ERROR)

file_handler.setFormatter(formatter)

steamer_handler = logging.StreamHandler()
steamer_handler.setFormatter(formatter)

logger.addHandler(file_handler)
logger.addHandler(steamer_handler)


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    try:
        result = x / y
    except ZeroDivisionError:
        logger.exception("Tried to divide by zero")
    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.info("Add: {} + {} = {}".format(num_1, num_2, add_result))

subtract_result = subtract(num_1, num_2)
logger.info("Subtract: {} - {} = {}".format(num_1, num_2, subtract_result))

multiply_result = multiply(num_1, num_2)
logger.info("Multiply: {} * {} = {}".format(num_1, num_2, multiply_result))

divide_result = divide(num_1, num_2)
logger.info("Divide: {} / {} = {}".format(num_1, num_2, divide_result))
