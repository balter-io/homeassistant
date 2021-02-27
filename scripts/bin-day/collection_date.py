#!usr/bin/env python3
from datetime import date, timedelta


def collection_date():
    """ Determine the bin collection date. """

    today = date.today()
    if today.weekday() > 3:		# normal collection day is thursday (day 3 of a zero-indexed week)
        today += timedelta((0 - today.weekday()) % 7)   # if thursday has passed, we only care about next week

    next_date = today + timedelta((3 - today.weekday()) % 7)  # set the collection date to next thursday
    collection = next_date.strftime('%d-%b-%Y')

    print(collection)
    return collection


if __name__ == '__main__':
    collection_date()