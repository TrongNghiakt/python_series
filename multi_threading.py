import time
import random
from concurrent.futures import ThreadPoolExecutor

tables = ["orders", "customers", "products", "employees", "suppliers"]


def my_func(i):
    # wait = random.randint(1, 10)
    wait = 3
    time.sleep(wait)
    print(f"I am {i}. I took {wait} seconds")


with ThreadPoolExecutor(max_workers=len(tables)) as executor:
    for i in tables:
        future = executor.submit(my_func, i)
