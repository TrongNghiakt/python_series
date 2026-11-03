# # File objects

# # f = open("D:\\python_learning\\test.txt", 'r')
# # print(f.mode)
# # f.close()

# with open("D:\\python_learning\\test.txt", 'r') as f:
#     # for line in f:
#     #     print(line, end='')
#     # f_contents = f.readline()
#     # print(f_contents, end='')

#     # f_contents = f.read(100)
#     # print(f_contents, end='')

#     # f_contents = f.read(100)
#     # print(f_contents, end='')

#     # size_to_read = 10
#     # f_contents = f.read(size_to_read)
#     # print(f_contents, end='')

#     # f.seek(0)

#     # f_contents = f.read(size_to_read)
#     # print(f_contents)

#     # print(f.tell())

#     # while len(f_contents) > 0:
#     #     print(f_contents, end='*')
#     #     f_contents = f.read(size_to_read)

#     f.write("Hello, World!")  # Failed


# with open("D:\\python_learning\\test2.txt", 'w') as f:
#     f.write('Test')
#     f.seek(0)
#     f.write('R')


# with open("D:\\python_learning\\test.txt", 'r') as rf:
#     with open("D:\\python_learning\\test_copy.txt", 'w') as wf:
#         for line in rf:
#             wf.write(line)


# with open("D:\\python_learning\\brox.jpg", 'rb') as rf:
#     with open("D:\\python_learning\\brox_copy.jpg", 'wb') as wf:
#         for line in rf:
#             wf.write(line)


with open("D:\\python_learning\\brox.jpg", 'rb') as rf:
    with open("D:\\python_learning\\brox_copy.jpg", 'wb') as wf:
        chunk_size = 4096
        rf_chunk = rf.read(chunk_size)
        while len(rf_chunk) > 0:
            wf.write(rf_chunk)
            rf_chunk = rf.read(chunk_size)
