import requests
from pprint import pprint


class TestUsers:

    def test_check_status_code(self):
        get_request = requests.get("https://reqres.in/api/users?page=2")
        actual_status_code = get_request.status_code
        assert actual_status_code == 200, "status code is not 200"

    def test_first_name_of_first_user(self):
        get_request = requests.get("https://reqres.in/api/users?page=2")
        body_users = get_request.json()
        actual_first_users_name =  body_users["data"][0]["first_name"]
        assert actual_first_users_name == "Michael", "name is not correct"


