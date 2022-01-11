class Swings:
    """This class holds the Swing variables and variable names to be plotted"""
    def __init__(self):
        self.names, self.vars = [], [[]]

    def input_num_of_vars(self):
        """Returns the number of variables inputted by the user"""
        num_of_vars = int(input("How many swing metrics would you like to graph? "))  # Get input from user
        while num_of_vars > 5:  # Ensure input value is less than 5
            print("The maximum number of swing metrics is 5!")  # print message if invalid number entered
            num_of_vars = int(input("How many swing metrics would you like to graph? "))  # retry input
        return num_of_vars

    def input_swing_metrics(self, num_of_vars):
        """Receives user input for each swing metric and appends to self.names; the size of self.vars is appropriately
                determined"""
        for i in range(num_of_vars):  # iterate num_of_vars times
            var_name = str(input("Enter a swing metric: "))  # get user input
            self.names.append(var_name)  # append to self.names
            self.vars.append([])  # append list to self.vars

    def generate_var_name(self, var_name):
        """Return properly formatted variable name to look up"""
        string_split = var_name.split()  # Split input value
        string_split = [str(word).lower().capitalize() for word in string_split]  # Adjust each word to capitalize only first letter
        if string_split[0] == "Avg":
            string_split[0] = "Average"  # extend abbreviation
        elif string_split[0] == "Max":
            string_split[0] = "Maximum"  # extend abbreviation
        if ("Bat" in string_split) and ("Speed" in string_split) and ("(mph)" not in string_split):
            string_split.append("(mph)")  # add "(mph)" if missing
        return ' '.join(string_split)  # return string

    def load_vars(self, date):
        """Load data values for each variable"""
        for i in range(len(self.names)):  # for num of variables
            self.names[i] = self.generate_var_name(self.names[i])  # generate var_name in proper formatting
            data_label = self.generate_data_label(self.names[i])  # generate data_label matching SWING_PATH format
            if "Average" in self.names[i]:
                self.vars[i].append(date.get_avg_value(data_label))  # call get_avg_value if "Average"
            elif "Maximum" in self.names[i]:
                self.vars[i].append(date.get_max_value(data_label))  # call get_max_value if "Maximum"

    def generate_data_label(self, var_name):
        """Returns data_label ignoring "Average" and "Maximum"."""
        data_label = var_name.split()  # split
        if data_label[0] == "Average" or data_label[0] == "Maximum":  # if begins with Average or Maximum
            data_label = data_label[1:]  # ignore first word
        return ' '.join(data_label)  # return string

