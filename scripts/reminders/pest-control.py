#!/usr/bin/env python3
from datetime import timedelta, date, datetime
import calendar


def pest_control():

    inspection = date(2020, 1, 14)
    current_date = datetime.now()
    current_year = current_date.year

    while inspection != date.today():

        if calendar.isleap(current_year):
            twelve_months = inspection + timedelta(days=366)
        else:
            twelve_months = inspection + timedelta(days=365)
        print(twelve_months.strftime('%d-%b-%Y'))
        break
    else:
        print(date.today().strftime('%d-%b-%Y'))


pest_control()
