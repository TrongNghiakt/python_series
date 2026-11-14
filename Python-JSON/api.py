import json
from urllib.request import urlopen

with urlopen("https://api.frankfurter.dev/v2/rates?base=USD&quotes=EUR,GBP") as response:
    source = response.read()

data = json.loads(source)

print(json.dumps(data, indent=2))
