#!usr/bin/env python3
from datetime import date, datetime, timedelta
from waste_resources.requests import WasteRequests


def collection_type():
    """
    Uses the Brisbane City Council API to determine the bin collection type each week
    https://www.data.brisbane.qld.gov.au/data/dataset/a3d075b9-70d7-40b3-a693-70db2a415765/resource/10699d57-3a21-4b07-b819-38ae62a9bffc/download/wca_2019-12-02.txt
    """

    weeks = WasteRequests()
    bin_type = None

    for week in weeks.get_week_request()['result']['records']:
        zone = week['ZONE']
        collection_date = datetime.strptime(week['WEEK_STARTING'], '%d/%m/%Y').date() + timedelta(days=3)

        if date.today() > collection_date:
            continue

        if date.today() == collection_date:
            bin_type = 'Recycling' if weeks.get_day_request()['result']['records'][0]['ZONE'] == \
                zone else 'Garden waste'
            print(f'Landfill and {bin_type}')
            break

        if date.today() < collection_date:
            bin_type = 'Recycling' if weeks.get_day_request()['result']['records'][0]['ZONE'] == \
                zone else 'Garden waste'
            print(f'Landfill and {bin_type}')
            break


if __name__ == '__main__':
    collection_type()

