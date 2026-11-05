# # def square_numbers(nums):
# #     for i in nums:
# #         yield (i * i)


# # my_nums = square_numbers([1, 2, 3, 4, 5])

# my_nums = (x*x for x in [1, 2, 3, 4, 5])

# # print(next(my_nums))
# print(list(my_nums))

# # for num in my_nums:
# #     print(num)


import time
import random
import memory_profiler as mem_profile

names = ['John', 'Corey', 'Adam', 'Steve', 'Rick', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']

print("Memory (Before): {} MiB".format(mem_profile.memory_usage()[0]))


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        result.append(person)
    return result


def people_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(names),
            'major': random.choice(majors)
        }
        yield person


t1 = time.perf_counter()
people = people_list(1000000)
t2 = time.perf_counter()

print("Memory (After): {} MiB".format(mem_profile.memory_usage()[0]))
print("Took {} Seconds".format(t2-t1))
