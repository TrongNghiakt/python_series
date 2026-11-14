# Context Managers - Efficiently Managing Resources

from contextlib import contextmanager
import os

# class Open_File():
#     def __init__(self, filename, mode):
#         self.filename = filename
#         self.mode = mode

#     def __enter__(self):
#         self.file = open(self.filename, self.mode)
#         return self.file

#     def __exit__(self, exc_type, exc_value, traceback):
#         self.file.close()


# with Open_File('D:\\python_learning\\Python-Context-Managers\\sample.txt', 'w') as f:
#     f.write('Testing')
# print(f.closed)


# @contextmanager
# def open_file(filename, mode):
#     try:
#         f = open(filename, mode)
#         yield f
#     finally:
#         f.close()


# with open_file('D:\\python_learning\\Python-Context-Managers\\sample.txt', 'w') as f:
#     f.write('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.')

# print(f.closed)


# cwd = os.getcwd()
# os.chdir('D:\\python_learning\\Python-Context-Managers\\Sample-Dir-One')
# print(os.listdir())
# os.chdir(cwd)

# cwd = os.getcwd()
# os.chdir('D:\\python_learning\\Python-Context-Managers\\Sample-Dir-Two')
# print(os.listdir())
# os.chdir(cwd)


@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)


with change_dir('D:\\python_learning\\Python-Context-Managers\\Sample-Dir-One'):
    print(os.listdir())

with change_dir('D:\\python_learning\\Python-Context-Managers\\Sample-Dir-Two'):
    print(os.listdir())
