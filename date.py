import csv
import datetime

from config import SWING_PATH, WHOOP_PATH


class Date:
    def __init__(self, date):
        self.date = date
        self.swings = []
        self.health_data = None

        self.loadSwings()
        self.loadHealthData()

    def loadSwings(self):
        with open(SWING_PATH, mode='r', encoding='utf-8-sig') as swingFile:
            swings = csv.DictReader(swingFile)
            for swing in swings:
                if self.date in datetime.datetime.strptime(swing.get("Date"), "%b %d, %Y %H:%M:%S %p").strftime("%Y-%m-%d"):
                    self.swings.append(swing)

    def loadHealthData(self):
        with open(WHOOP_PATH, mode='r', encoding='utf-8-sig') as healthFile:
            health_data = csv.DictReader(healthFile)
            for data in health_data:
                if self.date in datetime.datetime.strptime(data.get("Date"), "%Y-%m-%d").strftime("%Y-%m-%d"):
                    self.health_data = data

    def avgBatSpeed(self):
        total_bat_speed = 0
        for swing in self.swings:
            total_bat_speed += float(swing.get("Bat Speed (mph)"))
        return total_bat_speed / len(self.swings)

    def maxBatSpeed(self):
        max_bat_speed = 0
        for swing in self.swings:
            if float(swing.get("Bat Speed (mph)")) > max_bat_speed:
                max_bat_speed = float(swing.get("Bat Speed (mph)"))
        return max_bat_speed
