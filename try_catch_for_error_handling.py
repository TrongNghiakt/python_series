# f = open('D:\\python_learning\\csv\\test_file.txt')


try:
    # f = open('D:\\python_learning\\csv\\test_file.txt')
    f = open('D:\\python_learning\\csv\\currupt_file.txt')
    # if f.name == 'D:\\python_learning\\csv\\currupt_file.txt':
    #     raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error: File is currupted')
else:
    print(f.read())
    f.close()
finally:
    print('Executing finally....')
