import requests
import variables as env


class WasteRequests:

    def __init__(self):
        self.day_request = env.day_api_variable()
        self.week_request = env.week_api_variable()

    def get_day_request(self):
        return requests.get(self.day_request).json()

    def get_week_request(self):
        return requests.get(self.week_request).json()
