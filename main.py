from util import read_swings
import plot

list_of_dates = read_swings()  # Generates a list of all dates in which swings were recorded
plot.main(list_of_dates)  # call to plot.main to generate necessary vars and create plots
