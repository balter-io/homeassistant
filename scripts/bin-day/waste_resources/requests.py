import requests

day = 'https://www.data.brisbane.qld.gov.au/data/api/3/action/datastore_search?resource_id=adcb0791-71f1-4b0e-bb6f-b375ac244896&q=529037'
week = 'https://www.data.brisbane.qld.gov.au/data/api/3/action/datastore_search?resource_id=c6dbb0b3-1e00-4bb8-8776-aa1b8f1ecfaa'


class WasteRequests:

    def __init__(self):
        self.day_request = day
        self.week_request = week

    def get_day_request(self):
        return requests.get(self.day_request).json()

    def get_week_request(self):
        return requests.get(self.week_request).json()
