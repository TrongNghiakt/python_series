from operator import attrgetter
li = [9, 2, 7, 1, 5, 3, 8, 4, 6]

s_li = sorted(li, reverse=False)

print('List Sorted variable:\t', s_li)

# li.sort()

print('Original variable:\t', li)

tup = (9, 2, 7, 1, 5, 3, 8, 4, 6)
s_tup = sorted(tup)
print('Tuple Sorted variable:\t', s_tup)


di = {'name': 'Corey', 'job': 'programmer', 'age': None, 'os': 'Mac'}

print('Dictionary Sorted variable:\t', sorted(di))


li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print('List Sorted variable:\t', s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return '({},{},${})'.format(self.name, self.age, self.salary)


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)

employees = [e1, e2, e3]


# def e_sort(emp):
#     return emp.salary


# s_employees = sorted(employees, key=lambda e: e.name, reverse=True)
s_employees = sorted(employees, key=attrgetter('name'), reverse=True)

print('Employees Sorted variable:\t', s_employees)
