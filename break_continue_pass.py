# Break, Continue, Pass statement
# names = ['john', 'maria', '', 'kumar']
# for name in names:
#     if name == '':
#         pass  # todo: Handle Empty Value
#         name = name.replace('', 'Unknown')
#     print(f"Name = {name}")


# Skip weekend days in calendar loop
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday', 'Sunday']
weekends = ['Saturday', 'Sunday']
for day in days:
    if day in weekends:
        continue  # Skip weekend days
    print(f"Working day = {day}")
