#!usr/bin/env python3
from datetime import date, timedelta
from waste_resources.requests import WasteRequests


def collection_type():
    """
    Uses the Brisbane City Council API to determine the bin collection type each week
    https://www.data.brisbane.qld.gov.au/data/dataset/a3d075b9-70d7-40b3-a693-70db2a415765/resource/10699d57-3a21-4b07-b819-38ae62a9bffc/download/wca_2019-12-02.txt
    """

    weeks = WasteRequests()
    today = date.today()
    bin_type = None

    week_starting = today + timedelta((0 - today.weekday()) % 7)  # calculates next monday

    for week in weeks.get_week_request()['result']['records']:
        if week['WEEK_STARTING'] == week_starting.strftime('%-d/%m/%Y'):
            week_zone = week['ZONE']
            bin_type = 'Recycling' if weeks.get_day_request()['result']['records'][0]['ZONE'] == \
                week_zone else 'Garden waste'
            print(f'Landfill & {bin_type}')
            break