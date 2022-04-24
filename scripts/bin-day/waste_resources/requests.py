import requests
import os


class WasteRequests:

    def __init__(self, day_url, week_url):
        self.day_request = day_url
        self.week_request = week_url

    def get_day_request(self):
        return requests.get(self.day_request).json()

    def get_week_request(self):
        return requests.get(self.week_request).json()
