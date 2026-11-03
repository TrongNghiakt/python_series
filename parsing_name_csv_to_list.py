# Parsing Names From a CSV to an HTML List
import csv

html_output = ''
names = []

with open('D:\\python_learning\\csv\\patrons.csv', 'r') as data_file:
    csv_data = csv.reader(data_file)

    for line in csv_data:
        print(line)
