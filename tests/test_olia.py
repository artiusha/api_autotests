import requests
from pprint import pprint

get_request = requests.get("https://reqres.in/api/users?page=2")
resp = get_request.status_code
raw_resp = get_request.json()

pprint(raw_resp)
