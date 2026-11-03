import csv

# with open('D:\\python_learning\\new_names.csv', 'r', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter='\t')

#     for line in csv_reader:
#         print(line)

# with open('D:\\python_learning\\name.csv', 'r', newline='') as csv_file:
#     csv_reader = csv.reader(csv_file)

#     # print(csv_reader)  # This will print the reader object, not the contents
#     # This will print the contents of the CSV file as a list of rows
#     # print(list(csv_reader))

#     # next(csv_reader)  # Skip the header row if there is one
#     with open('D:\\python_learning\\new_names.csv', 'w', newline='') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#         for line in csv_reader:
#             csv_writer.writerow(line)


# Using DictReader to read and write CSV file as dictionaries
# with open('D:\\python_learning\\name.csv', 'r', newline='') as csv_file:
#     csv_reader = csv.DictReader(csv_file)

#     for line in csv_reader:
#         print(line['email'])


with open('D:\\python_learning\\name.csv', 'r', newline='') as csv_file:

    csv_reader = csv.DictReader(csv_file)
    with open('D:\\python_learning\\new_names.csv', 'w', newline='') as new_file:
        fieldnames = ['first_name', 'last_name']

        csv_writer = csv.DictWriter(
            new_file, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['email']  # Remove the 'email' field from the dictionary
            csv_writer.writerow(line)
