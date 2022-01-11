from util import read_swings
import plot


def choose_mode():
    """Returns the type of graph that the user wants to appear"""
    print("This program supports a number of different graph styles. You can either graph multiple variables over "
          "time or compare two variables directly.\nEnter 'time' to graph multiple lines with dates over the x-axis "
          "or enter 'compare' to graph one variable on the x-axis and the other on the y-axis.")
    mode = str(input("Choose your mode: ")).lower().strip()
    while mode != 'time' and mode != 'compare':
        print("Your mode appears to be invalid. Please try again.")
        mode = str(input("Choose your mode: ")).lower().strip()
    return mode


list_of_dates = read_swings()  # Generates a list of all dates in which swings were recorded
if choose_mode() == 'time':
    my_plot = plot.Plot()  # new Plot
    my_plot.health.input_health_metrics(my_plot.health.input_num_of_vars())  # Helper functions
    my_plot.swings.input_swing_metrics(my_plot.swings.input_num_of_vars())
    my_plot.load_vars(list_of_dates)
    my_plot.generate_graph(len(my_plot.health.names), len(my_plot.swings.names))  # Generate graph
else:
    my_plot = plot.Plot()
    my_plot.health.input_health_metrics(1)  # Helper functions
    my_plot.swings.input_swing_metrics(1)
    my_plot.load_vars(list_of_dates)
    # build new method to generate compare graph
    my_plot.generate_compare_graph()  # try to unify with generate_graph
