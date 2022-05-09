import requests
import os


class WasteRequests:

    def __init__(self):
        self.day_request = os.environ.get('day')
        self.week_request = os.environ.get('week')

    def get_day_request(self):
        return requests.get(self.day_request).json()

    def get_week_request(self):
        return requests.get(self.week_request).json()
