#!usr/bin/env python3
from datetime import date, timedelta
from waste_resources.requests import WasteRequests


def collection_type():
    weeks = WasteRequests()
    today = date.today()

    if today.weekday() > 3:  # if this thursday has passed, we only care about next week
        week_starting = today + timedelta((0 - today.weekday()) % 7)  # calculates next monday

        for week in weeks.get_week_request()['result']['records']:
            if week['WEEK_STARTING'] == week_starting.strftime('%d/%m/%Y'):
                week_zone = week['ZONE']

                bin_type = 'Recycling' if weeks.get_day_request()['result']['records'][0]['ZONE'] == week_zone else 'Garden waste'

                print(f'Landfill & {bin_type}')


if __name__ == '__main__':
    collection_type()
