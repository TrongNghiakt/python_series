import os
import requests

# Call API
response = requests.get(
    "https://jsonplaceholder.typicode.com/posts/1?utm_source=chatgpt.com")

print(response.status_code)
print(response)

data = response.json()
print(data)


# OS Module
os.makedirs("")
