import matplotlib.pyplot as plt
import numpy as np

from health import Health
from swings import Swings


class Plot:
    """This class is a plot"""
    def __init__(self, list_of_dates):
        self.dates = []

        self.list_of_dates = list_of_dates
        self.health = Health()
        self.num_of_health_vars = self.health.input_num_of_vars()

        self.swings = Swings()
        self.num_of_swing_vars = self.swings.input_num_of_vars()

    def load_vars(self):
        """Appends each date and calls load_vars helpers for health and swings"""
        for date in self.list_of_dates:
            self.dates.append(date.date)  # append date
            self.health.load_vars(date)  # call helper
            self.swings.load_vars(date)  # call helper

    def generate_graph(self, num_of_health_vars, num_of_swing_vars):
        """Generates, plots, and shows graph"""
        fig, ax = plt.subplots()
        # fig.subplots_adjust(right=0.75)X

        twin1 = ax.twinx()
        x = np.array(self.dates)

        lines_plotted = []  # tracks all lines plotted to include in legend

        # Generate num of plots based on num of vars
        if num_of_health_vars > 0:
            h1, = ax.plot(x, self.health.vars[0], "b-", label=self.health.names[0])
            lines_plotted.append(h1)
        if num_of_health_vars > 1:
            h2, = ax.plot(x, self.health.vars[1], "g-", label=self.health.names[1])
            lines_plotted.append(h2)
        if num_of_health_vars > 2:
            h3, = ax.plot(x, self.health.vars[2], "r-", label=self.health.names[2])
            lines_plotted.append(h3)
        if num_of_health_vars > 3:
            h4, = ax.plot(x, self.health.vars[3], "c-", label=self.health.names[3])
            lines_plotted.append(h4)
        if num_of_health_vars > 4:
            h5, = ax.plot(x, self.health.vars[4], "m-", label=self.health.names[4])
            lines_plotted.append(h5)
        if num_of_swing_vars > 0:
            s1, = twin1.plot(x, self.swings.vars[0], "y-", label=self.swings.names[0])
            lines_plotted.append(s1)
        if num_of_swing_vars > 1:
            s2, = twin1.plot(x, self.swings.vars[1], "m-", label=self.swings.names[1])
            lines_plotted.append(s2)
        if num_of_swing_vars > 2:
            s3, = twin1.plot(x, self.swings.vars[2], "c-", label=self.swings.names[2])
            lines_plotted.append(s3)
        if num_of_swing_vars > 3:
            s4, = twin1.plot(x, self.swings.vars[3], "r-", label=self.swings.names[3])
            lines_plotted.append(s4)
        if num_of_swing_vars > 4:
            s5, = twin1.plot(x, self.swings.vars[4], "g-", label=self.swings.names[4])
            lines_plotted.append(s5)

        # y-axes ranges
        ax.set_ylim(0, 100)
        twin1.set_ylim(60, 80)

        # Find ways to generate labels based on data chosen by user
        # i.e. Health data on left (ax, ax2, ax3, etc.), and swing data on right (twin1, twin2, etc.)

        ax.set_xlabel("Date")  # x-axis label
        ax.set_ylabel("Percent")  # y-axis label 1
        twin1.set_ylabel("Bat Speed (mph)")  # y-axis label 2

        plt.title("Relationship between Sleep Scores and Bat Speed")  # plot title
        plt.legend(handles=lines_plotted)  # legend key

        plt.show()  # show plot
