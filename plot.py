import matplotlib.pyplot as plt
import numpy as np


'''Variables'''
dates, sleep_scores, avg_bat_speed_list, max_bat_speed_list = [], [], [], []
health_var0, health_var1, health_var2, health_var3, health_var4, = [], [], [], [], []
swing_var0, swing_var1, swing_var2, swing_var3, swing_var4 = [], [], [], [], []
health_vars = [health_var0, health_var1, health_var2, health_var3, health_var4]
swing_vars = [swing_var0, swing_var1, swing_var2, swing_var3, swing_var4]
health_var_names, swing_var_names = [], []


def input_health_metrics(num_of_health_vars):
    for i in range(num_of_health_vars):
        health_var_name = str(input("Enter a health metric: "))
        health_var_names.append(health_var_name)


def input_swing_metrics(num_of_swing_vars):
    for i in range(num_of_swing_vars):
        swing_var_name = input("Enter a swing metric: ")
        swing_var_names.append(swing_var_name)


def generate_graph(num_of_health_vars, num_of_swing_vars):
    fig, ax = plt.subplots()
    # fig.subplots_adjust(right=0.75)X

    twin1 = ax.twinx()
    x = np.array(dates)

    lines_plotted = []

    if num_of_health_vars > 0:
        h1, = ax.plot(x, health_vars[0], "b-", label=health_var_names[0])
        lines_plotted.append(h1)
    if num_of_health_vars > 1:
        h2, = ax.plot(x, health_vars[1], "g-", label=health_var_names[1])
        lines_plotted.append(h2)
    if num_of_health_vars > 2:
        h3, = ax.plot(x, health_vars[2], "r-", label=health_var_names[2])
        lines_plotted.append(h3)
    if num_of_health_vars > 3:
        h4, = ax.plot(x, health_vars[3], "c-", label=health_var_names[3])
        lines_plotted.append(h4)
    if num_of_health_vars > 4:
        h5, = ax.plot(x, health_vars[4], "m-", label=health_var_names[4])
        lines_plotted.append(h5)
    if num_of_swing_vars > 0:
        s1, = twin1.plot(x, swing_vars[0], "y-", label=swing_var_names[0])
        lines_plotted.append(s1)
    if num_of_swing_vars > 1:
        s2, = twin1.plot(x, swing_vars[1], "m-", label=swing_var_names[1])
        lines_plotted.append(s2)
    if num_of_swing_vars > 2:
        s3, = twin1.plot(x, swing_vars[2], "c-", label=swing_var_names[2])
        lines_plotted.append(s3)
    if num_of_swing_vars > 3:
        s4, = twin1.plot(x, swing_vars[3], "r-", label=swing_var_names[3])
        lines_plotted.append(s4)
    if num_of_swing_vars > 4:
        s5, = twin1.plot(x, swing_vars[4], "g-", label=swing_var_names[4])
        lines_plotted.append(s5)

    ax.set_ylim(0, 100)
    twin1.set_ylim(60, 80)

    # Find ways to generate labels based on data chosen by user
    # i.e. Health data on left (ax, ax2, ax3, etc.), and swing data on right (twin1, twin2, etc.)

    ax.set_xlabel("Date")
    ax.set_ylabel("Percent")
    twin1.set_ylabel("Bat Speed (mph)")

    plt.title("Relationship between Sleep Scores and Bat Speed")
    plt.legend(handles=lines_plotted)

    plt.show()


def load_vars(list_of_dates, num_of_health_vars, num_of_swing_vars):
    for date in list_of_dates:
        dates.append(date.date)
        for i in range(num_of_health_vars):
            try:
                health_vars[i].append(float(date.health_data.get(health_var_names[i])))
            except AttributeError:  # Data value does not exist
                health_vars[i].append(0.0)
        for i in range(num_of_swing_vars):
            if swing_var_names[i] == "Average Bat Speed":
                swing_vars[i].append(date.avgBatSpeed())
            elif swing_var_names[i] == "Maximum Bat Speed":
                swing_vars[i].append(date.maxBatSpeed())


def main(list_of_dates):
    num_of_health_vars = int(input("How many health metrics would you like to graph? "))  # Must be ≤ 5
    while num_of_health_vars > 5:
        print("The maximum number of health metrics is 5!")
        num_of_health_vars = int(input("How many health metrics would you like to graph? "))
    input_health_metrics(num_of_health_vars)

    num_of_swing_vars = int(input("How many swing metrics would you like to graph? "))
    while num_of_swing_vars > 5:
        print("The maximum number of swing metrics is 5!")
        num_of_swing_vars = int(input("How many swing metrics would you like to graph? "))
    input_swing_metrics(num_of_swing_vars)

    load_vars(list_of_dates, num_of_health_vars, num_of_swing_vars)
    generate_graph(num_of_health_vars, num_of_swing_vars)
