import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


class AutomationInTestingAPIClient:
    def __init__(self):
        self.token = ''

    def get_token(self, username, password):
        url = 'https://restful-booker.herokuapp.com/auth'
        headers = {'Accept': 'application/json'}
        json = {
            'username': username,
            'password': password
        }
        response = requests.post(
            url, headers=headers, json=json, verify=False)

        self.token = response.text

    def ping_endpoint(self):
        url = 'https://restful-booker.herokuapp.com/ping'
        headers = {'Accept': 'application/json'}

        response = requests.get(
            url, headers=headers, verify=False)

        return {
            'status': response.status_code
        }

    def get_booking_id_endpoint(self, endpoint, id):
        url = f'https://restful-booker.herokuapp.com/{endpoint}/{id}'
        headers = {'Accept': 'application/json'}

        response = requests.get(
            url, headers=headers, verify=False)

        return {
            'body': response.text,
            'status': response.status_code
        }
