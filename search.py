# Search
# phone = "+48-176-12345"
# print(phone.startswith("+49"))

# email = "baraagmail.com"
# print(email.endswith("@gmail.com"))

# print("@" in email)

# url = "https://api.company.com/v1/data"
# print("api" in url)

phone1 = "+48-176-12345"
phone2 = "48-651-23634"
phone3 = "0048-651-23634"
print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])
print(phone3[phone3.find("-")+1:])
