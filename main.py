from util import read_swings
import plot

list_of_dates = read_swings()  # Generates a list of all dates in which swings were recorded
my_plot = plot.Plot(list_of_dates)  # new Plot
my_plot.health.input_health_metrics(my_plot.num_of_health_vars)  # Helper functions
my_plot.swings.input_swing_metrics(my_plot.num_of_swing_vars)
my_plot.load_vars()
my_plot.generate_graph(my_plot.num_of_health_vars, my_plot.num_of_swing_vars)  # Generate graph
