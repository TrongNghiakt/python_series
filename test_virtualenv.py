
import sys
import requests

print("Python executable:", sys.executable)
print("Requests version:", requests.__version__)

response = requests.get("https://httpbin.org/get", timeout=10)

print("Status code:", response.status_code)
print("Response:", response.json()["url"])
