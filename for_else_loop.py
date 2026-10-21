# items = [1, 3, 5, 7]
# for i in items:
#     if i % 2 == 0:
#         print("Even number:", i)
#         break
# else:
#     print("All numbers are odd")

files = ['data1.csv', 'report.pdf', 'report2.csv']
for file in files:
    if file.endswith('.csv'):
        print("CSV file found:", file)
        break
