

import requests

r = requests.get("https://useitnu.com")
print(r.status_code)
print(r.ok)
