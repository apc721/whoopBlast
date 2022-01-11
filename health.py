class Health:
    """This class holds the Health variables and variable names to be plotted"""
    def __init__(self):
        """Initialize variables"""
        self.names, self.vars = [], []

    def input_num_of_vars(self):
        """Returns the number of variables inputted by the user"""
        num_of_vars = int(input("How many health metrics would you like to graph? "))  # get input from user
        while num_of_vars > 5:  # ensure input value is less than 5
            print("The maximum number of health metrics is 5!")  # print error message
            num_of_vars = int(input("How many health metrics would you like to graph? "))  # retry input
        return num_of_vars

    def input_health_metrics(self, num_of_vars):
        """Receives user input for each swing metric and appends to self.names; the size of self.vars is appropriately
                determined"""
        for i in range(num_of_vars):  # iterate num_of_vars times
            var_name = str(input("Enter a health metric: "))  # get user input
            self.names.append(var_name)  # append to self.names
            self.vars.append([])  # append list to self.vars

    def load_vars(self, date):
        """Load data values for each variable"""
        for i in range(len(self.names)):  # for num of variables
            self.names[i] = self.generate_var_name(self.names[i])  # generate var_name in proper formatting
            try:
                self.vars[i].append(float(date.health_data.get(self.names[i])))  # append health data value
            except AttributeError:  # Data value does not exist
                self.vars[i].append(0.0)  # append 0.0 if not found

    def generate_var_name(self, var_name):
        """Return properly formatted variable name to look up"""
        string_split = var_name.split()  # Split input value
        string_split = [str(word).lower().capitalize() for word in string_split]  # capitalize only first letter of each word
        return ' '.join(string_split)  # return string
