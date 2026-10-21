# def multiple(x): return x*2
# print(multiple(5))  # Output: 10

# def add(x, y): return x + y
# print(add(3, 5))  # Output: 8

# check = lambda i: i in "Python"
# print(check("z"))


# prices = ['$12.50', '$9.99', '$100.00']
# # p = '$12.50'
# # print(type(float(p.replace('$', ''))))
# print(list(map(lambda p: float(p.replace('$', '')), prices)))


# prices = [120, 30, 80, 300]
# print(list(filter(lambda x: x >= 100, prices)))


students = [['Maria', 85], ['Kumar', 90], ['John', 70], ['Alice', 60]]

print(list(filter(lambda row: row[0].startswith('M'), students)))
print(list(s for s in students if s[0].startswith('M')))
