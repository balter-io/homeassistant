#!usr/bin/env python3
from datetime import date, timedelta


def collection_date():
    """ Determine the bin collection date. """

    today = date.today()
    next_date = today + timedelta((3 - today.weekday()) % 7)  # set the next collection date (next thursday)

    if date.weekday(today) > 3:		# normal collection day is thursday (day 3 of a zero-indexed week)
        print(next_date.strftime('%d-%b-%Y'))
    else:
        print(next_date.strftime('%d-%b-%Y'))


if __name__ == '__main__':
    collection_date()
