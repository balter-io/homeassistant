#!usr/bin/env python3
from datetime import date, timedelta


def collection_date():
    """ Determine the next bin collection date. """

    today = date.today()
    next_date = today + timedelta((3 - today.weekday()) % 7)  # calculate the next collection date (next thursday)

    if next_date == today:
        next_date = today + timedelta(7)  # if today is the collection date, add 7 days to get next weeks date
    print(next_date.strftime('%d-%b-%Y'))


if __name__ == '__main__':
    collection_date()
