import numpy as np
import pandas as pd


class CleanlockHolmes:
    """
    represents dataset objects in the process of being cleaned. Provides
    effective and straightforward approach to handling invalid values in
    datasets.
    """
    
    def __init__(self,file_name):
        self.file_name = file_name
        self.data_object = self.read_data(file_name)
        self.columns = self.data_object.columns
        self.invalid_dictionary = {}
        self.valid_dictionary = {}
    

    def read_data(self, input_file):
    """
    Function to read data from an input file and stores it in a pandas DataFrame
    param input_file: input file from user
    returns None
    """
        file_name, file_format = input_file.split(".")

        if file_format == 'csv':
        
            df = pd.read_csv(input_file)

        elif file_format == 'json':

            df = pd.read_json(input_file)

        else:
            df = None
            print("Data type not supported by this package")

        return df

    def specify_invalid_entries(self, invalid_values_list, col_name):
        """
        Function allowing user to declare a list of invalid value entries
        for a specifed column
        param:
                invalid_values_list - list of invalid value entries
                col_name - specified column
        returns None

        """
        pass

    def specify_valid_entries(self,valid_values_list, col_name):
        """
        Function allowing user to declare a list of valid value entries
        for a specifed column. 
        param:
                valid_values_list - list of valid value entries
                col_name - specified column
        returns None

        """

        pass

    def clean_data(self, method, arg = {}):

        """
        Function utalizes chosen method to rectify problematic value entries.
        Selects a method from these options:
        method 1 drop_row: removes data point
        method 2 replace_row : replaces problematic data point with values
        specified in arg["replacement"]
        method 3 interpolation : (TO DO)
        param

                method - rectification method specified by user
                arg - dictionary containg replacement options
        returns None

        """

        pass

    def write_data(self, new_file_name):

        """
        Function writes rectified data to a specified file
        param new_file_name: specified file
        returns None
        """
        
