import os
from datetime import datetime

# print(dir(os))
# print(os.getcwd())

# os.chdir('D:/python_learning/import_module_and_exploring_the_standard_library')

# print(os.getcwd())

# print(os.listdir())

# os.mkdir('OS-Demo-2')
# os.makedirs('OS-Demo-2/Sub-Dir-1/Sub-Sub-Dir-1')

# os.rmdir('OS-Demo-2')
# os.removedirs('OS-Demo-2/Sub-Dir-1/Sub-Sub-Dir-1')
# os.removedirs('OS-Demo-2')

# file = open('test.txt', 'w')
# file.close()

# os.rename('test.txt', 'demo.txt')

# print(os.stat('demo.txt')
# print(os.stat('demo.txt').st_size)

# mod_time=os.stat('demo.txt').st_mtime
# print(datetime.fromtimestamp(mod_time))

# print(os.listdir())

# for dirpath, dirnames, filenames in os.walk('D:/Study/KLTN/05_CLC_HTTT_XayDungWebsiteBanSachTichHopAI'):
#     print('Current Path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:', filenames)
#     print()


# print(os.environ.get('TMP'))

# file_path=os.path.join(os.environ.get('TMP'), 'demo.txt')
# print(file_path)


print(os.path.basename('/tmp/test.txt'))

print(os.path.dirname('/tmp/test.txt'))

print(os.path.split('/tmp/test.txt'))

print(os.path.exists('/tmp/test.txt'))

print(os.path.isdir('/tmp/tasdfasdf'))

print(os.path.isfile('/tmp/tasdfasdf.txt'))

print(os.path.splitext('/tmp/tasdfasdf.txt'))

print(dir(os.path))
