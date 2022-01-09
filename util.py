import csv
import datetime

import plot
from config import SWING_PATH
from date import Date

list_of_dates = []


def read_swings(path=SWING_PATH):
    with open(path, mode='r', encoding='utf-8-sig') as swing_metrics:
        rows = csv.DictReader(swing_metrics)
        for row in rows:
            if len(list_of_dates) == 0:
                list_of_dates.append(
                    Date(datetime.datetime.strptime(row.get("Date"), "%b %d, %Y %H:%M:%S %p").strftime("%Y-%m-%d")))
            else:
                date_found = False
                for date in list_of_dates:
                    if datetime.datetime.strptime(row.get("Date"), "%b %d, %Y %H:%M:%S %p").strftime("%Y-%m-%d") == date.date:
                        date_found = True
                        break
                if not date_found:
                    list_of_dates.append(Date(datetime.datetime.strptime(row.get("Date"), "%b %d, %Y %H:%M:%S %p").strftime("%Y-%m-%d")))


def call_plot():
    plot.main(list_of_dates)
