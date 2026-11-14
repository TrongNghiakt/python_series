'''JavaScript Object Notation'''
import json

# people_string = '''
# {
#     "people": [
#     {
#         "name":"John Smith",
#         "phone":"615-555-7164",
#         "email":["johnsmith@bogusemail.com","john.smith@work-place.com"],
#         "has_license":false
#     },
#     {
#         "name":"Jane Doe",
#         "phone":"560-555-5153",
#         "email":null,
#         "has_license":true
#     }
#     ]
# }
# '''

# data = json.loads(people_string)
# # print(type(data['people']))

# for person in data['people']:
#     del person['phone']

# new_string = json.dumps(data, indent=2, sort_keys=True)
# print(new_string)


with open('D:\\python_learning\\Python-JSON\\states.json') as f:
    data = json.load(f)


for state in data['states']:
    del state['area_codes']

with open("D:\\python_learning\\Python-JSON\\new_states.json", "w") as f:
    json.dump(data, f, indent=2)
