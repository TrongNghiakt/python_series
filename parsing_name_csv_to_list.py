# Parsing Names From a CSV to an HTML List
import csv

html_output = ''
names = []

with open('D:\\python_learning\\csv\\patrons.csv', 'r') as data_file:
    csv_data = csv.DictReader(data_file)

    # We don't want headers or first line of bad daba
    next(csv_data)  # Skip the header row

    for line in csv_data:
        if line['FirstName'] == 'No Reward':
            break
        names.append(f"{line['FirstName']} {line['LastName']}")

html_output += f'<p> There are currently {len(names)} public contributors. Thank You!</p>'

html_output += '<ul>'

for name in names:
    html_output += f'\n\t<li>{name}</li>'

html_output += '\n</ul>'

print(html_output)
