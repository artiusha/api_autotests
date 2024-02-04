import requests
from pprint import pprint


# raw_resp = get_request.json()


def test_check_status_code():
    get_request = requests.get("https://reqres.in/api/users?page=2")
    actual_status_code = get_request.status_code
    assert actual_status_code == 200, "status code is not 200"
