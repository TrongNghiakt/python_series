# person = {'name': 'Trung', 'age': 22}

# l = ['Jenn', 23]

# sentence = 'My name is ' + person['name'] + \
#     ' and I am ' + str(person['age']) + ' years old.'

# sentence = "My name is {0} and I am {1} years old.".format(
#     person['name'], person['age'])

# tag = 'h1'
# text = 'This is a headline'

# sentence = '<{0}>{1}</{0}>'.format(tag, text)

# sentence = 'My name is {0[0]} and I am {0[1]} years old.'.format(l)

# sentence = 'My name is {name} and I am {age} years old.'.format(
#     name='Nghia', age=22)


# Dict
# person = {'name': 'Trung', 'age': 22}

# sentence = 'My name is {name} and I am {age} years old.'.format(**person)

# print(sentence)


# for i in range(1, 11):
#     sentence = 'The value is {:03}'.format(i)
#     print(sentence)

# pi = 3.14159265
# sentence = 'Pi is equal to {:.2f}'.format(pi)
# print(sentence)


# sentence = '1 MB is equal to {:,.2f} bytes'.format(1000**2)
# print(sentence)


import datetime
my_date = datetime.datetime(2016, 3, 1, 12, 30, 45)
print(my_date)


# March 01, 2016
# sentence = '{:%B, %d, %Y}'.format(my_date)
# print(sentence)

# March 01, 2016 fell on a Tuesday and was the 61st day of the year.
sentence = '{0:%B, %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year.'.format(
    my_date)
print(sentence)
