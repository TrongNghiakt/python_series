x = 10
try:
    if x > 10:
        print("Greater than 10")
    else:
        print("Less than or equal to 10")
except Exception as e:
    print(f"Hey, yor got this error - {e}")
finally:
    print("I will allways run, no matter what!")
print("This is a test")


def my_func(x):
    try:
        if x % 2 == 0:
            return 1
    except Exception as e:
        return e
    finally:
        print("This is a test")


my_func(2)


x = 99
if x < 100:
    # raise ValueError("Hey, x should not be less than 100")
    raise Exception("Hey, x should not be less than 100")
