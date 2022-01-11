import csv
import datetime

from config import SWING_PATH, WHOOP_PATH


class Date:
    """This class holds a date value, and all swings and health_data from that date"""
    def __init__(self, date):
        """Initialize variables"""
        self.date = date
        self.swings = []
        self.health_data = None

        """Methods called by default"""
        self.loadSwings()  # loads all swings of same date
        self.loadHealthData()  # loads health data of same date

    def loadSwings(self):
        """Reads SWING_PATH (csv file) and appends each swing to a list of all swings"""
        with open(SWING_PATH, mode='r', encoding='utf-8-sig') as swingFile:  # open Blast file
            swings = csv.DictReader(swingFile)  # read csv and store values as dict
            for swing in swings:  # iterate through swings
                if self.date in datetime.datetime.strptime(swing.get("Date"), "%b %d, %Y %H:%M:%S %p").strftime(
                        "%Y-%m-%d"):
                    self.swings.append(swing)  # append swing if date equals date on Blast file

    def loadHealthData(self):
        """Reads WHOOP_PATH (csv file) and assigns data to self.health_data"""
        with open(WHOOP_PATH, mode='r', encoding='utf-8-sig') as healthFile:  # open Whoop file
            health_data = csv.DictReader(healthFile)  # read csv and store values as dict
            for data in health_data:  # iterate through health_data
                if self.date in datetime.datetime.strptime(data.get("Date"), "%Y-%m-%d").strftime("%Y-%m-%d"):
                    self.health_data = data  # assign this data if date equals date on whoop file
                    break

    def get_avg_value(self, value_name):
        """Returns the average value of chosen parameter"""
        total_value = 0  # variable to track totals of all values
        for swing in self.swings:  # iterate through all swings
            total_value += float(swing.get(value_name))  # total_value updated
        return total_value / len(self.swings)  # return the average

    def get_max_value(self, value_name):
        """Returns the maximum value of chosen parameter"""
        max_value = 0  # variable to track the maximum value
        for swing in self.swings:  # iterate through all swings
            if float(swing.get(value_name)) > max_value:  # if next value is greater than current max
                max_value = float(swing.get(value_name))  # update max_value
        return max_value
