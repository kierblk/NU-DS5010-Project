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
        self.col_types_dictionary = {}
        self.data_ranges = {}

    def interactive_specify_col_data_types(self):
        """
        User specifies data type for each column
        param self.columns column headers
        returns None
        """
        question = "Please enter a column data type:\nA = String\nB = Integer\nC = Float "

        for column in self.columns:
            print(f"Column name: {column}")
            user_input = input(question).upper()
            if user_input == "A":
                self.col_types_dictionary[column] = ['str']
            elif user_input == "B":
                self.col_types_dictionary[column] = ['int']
            else:
                self.col_types_dictionary[column] = ['float']

    def specify_col_data_types(self, data_type, col_name):
        """
        specification of data type for a given column
        param
            data_type: string representing data type of column (must be 'str', 'float' or 'int')
            col_name: name of column to specify
        returns None
        """
        self.col_types_dictionary[col_name] = [data_type]
        
    def read_data(self, input_file):
        """
        Function to read data from an input file and stores it in a pandas DataFrame
        param input_file: input file from user
        returns the dataframe if supported file otherwise none
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
        self.invalid_dictionary[col_name] = invalid_values_list
        
    def specify_valid_entries(self,valid_values_list, col_name):
        """
        Function allowing user to declare a list of valid value entries
        for a specifed column. 
        param:
                valid_values_list - list of valid value entries
                col_name - specified column
        returns None
        """
        self.valid_dictionary[col_name] = valid_values_list

    def _get_user_input_colbound(self, column):
        """
        Gets the user input used in calculating the viable range for numeric columns
        param Column : column name
        returns the min and max values specified by user, raises ValueErrror if non-numeric values are given
        """
        min_value = float(input(f"Please enter an numeric lower bound for {column}: "))
        max_value = float(input(f"Please enter an numeric upper bound for {column}: "))

        return min_value, max_value

    def interactive_specify_viable_range(self):
        """
        Specifies a viable column range of values where col is
        specified numeric 
        param None
        returns None
        """
        for column in self.columns:
            if self.col_types_dictionary[column] == ['int'] or self.col_types_dictionary[column] == ['float']:
                min_value = None
                max_value = None
                while type(min_value) != float or type(max_value) != float:
                    try:
                        min_value, max_value = self._get_user_input_colbound(column)

                    except:
                        print("only numeric values accepted")
                        min_value, max_value = self._get_user_input_colbound(column)
                        
                self.data_ranges[column] = [min_value, max_value]

    def specify_viable_range(self,min_value, max_value, col_name):
        """
        Specifies a viable column range of values  for a previously decalared numeric column
        raises ValueError if values are non-numeric or col_name had not been declared numeric
        param
            min_value: minimum value 
            max_value: maximum value
            col_name: column name
        returns None
        """    
        if col_name in self.col_types_dictionary and (self.col_types_dictionary[col_name] == ['int'] or self.col_types_dictionary[col_name] == ['float']):
            try:
                min_value = float(min_value)
                max_value = float(max_value)
                self.data_ranges[col_name] = [min_value, max_value]
                
            except ValueError:
                raise Exception("min and max values must be numeric")       
        else:
            raise Exception(f"column {col_name} must have been declared numeric prior to specifying viable range")

    def identify_invalid_values(self):
        """
        identifies row/col pairs that contain an invalid value 
        param None
        returns the invalid values tracker - row by columns numpy array where 0 denotes a valid entry and 1
        denotes an invalid entry
        """
        rows , columns = self.data_object.shape
        invalid_values_tracker = np.zeros((rows, columns))

        for j in range(len(self.columns)):
            col = self.columns[j]
            for i in range(rows):
                if type(type(self.data_object.loc[i].at[col])) == str:
                    self.data_object.loc[i].at[col] = self.data_object.loc[i].at[col].str.lower()
                if type(self.data_object.loc[i].at[col]) != str:
                    if np.isnan(self.data_object.loc[i].at[col]):
                        invalid_values_tracker[i][j] =1     
                if col in self.data_ranges:
                    if self.data_object.loc[i].at[col] < self.data_ranges[col][0] or self.data_object.loc[i].at[col] > self.data_ranges[col][1]:
                        invalid_values_tracker[i][j] =1               
                elif self.invalid_dictionary.get(col):
                    if self.data_object.loc[i].at[col] in self.invalid_dictionary[col]:
                        invalid_values_tracker[i][j] = 1
                elif self.valid_dictionary.get(col):
                    if self.data_object.loc[i].at[col] not in self.valid_dictionary[col]:
                        invalid_values_tracker[i][j] = 1
         
        return invalid_values_tracker

    def _clean_data_row_drop(self, invalid_values_tracker):
        """
        Function implements data cleaning method in which rows with invalid entries are dropped from the data frame
        param invalid_values_tracker represeting problematic values as 1 entries 
        returns None
        """
        rows, columns = invalid_values_tracker.shape
        for i in range(rows):
                total = sum(invalid_values_tracker[i])
                if total > 0:
                    self.data_object = self.data_object.drop([i])
        
    def _clean_data_replace_value(self, invalid_values_tracker, value_dictionary):
        """
        Function implements data cleaning method in which rows with invalid entries are replaced with specified values
        param:
            invalid_values_tracker represeting problematic values as 1 entries
            value_dictionary dictionary with column names as keys and replacement values as values
        returns None
        """
        rows, columns = invalid_values_tracker.shape
        for i in range(rows):
            for j in range(columns):
                col = self.columns[j]
                if invalid_values_tracker[i][j] == 1:
                    self.data_object.loc[i,col]= value_dictionary[col]
        
    def _clean_data_replace_average(self, invalid_values_tracker):
        """
        Function implements data cleaning method in which rows with numeric invalid entries are replaced with the median and
        non-numeric are replaced with a mode
        param:
            invalid_values_tracker represeting problematic values as 1 entries
        returns None
        """
        rows, columns = invalid_values_tracker.shape
        median_values = self.data_object.median(numeric_only = True)
        mode_values = self.data_object.mode().iloc[0]
        for j in range(columns):
            col = self.columns[j]
            if col in median_values:
                replace_value = median_values[col]
            else:
                replace_value = mode_values[col]
                                
            for i in range(rows):
                if invalid_values_tracker[i][j] == 1:
                    self.data_object.loc[i,col] = replace_value       

    def clean_data(self, method, invalid_values_tracker, arg = {}):
        """
        Function utilizes chosen method to rectify problematic value entries.
        Selects a method from these options:
        method 1 drop_row: removes data point
        method 2 replace_value : replaces problematic data point with values provided
        method 3 replace_average : replaces problematic numeric data point with the median and mode for categorical
        specified in arg (dictionary mapping col names to replacement values)
        param
                method - rectification method specified by user
                arg - dictionary containg auxiliary information (see method description for requirements)
        returns None
        """
        if method == 1:
            self._clean_data_row_drop(invalid_values_tracker)

        elif method == 2:
            self._clean_data_replace_value(invalid_values_tracker, arg)

        elif method == 3:
            self._clean_data_replace_average(invalid_values_tracker)

    def write_data(self, new_file_name):
        """
        Function writes rectified data to a specified file
        param new_file_name: specified file
        returns None
        """
        self.data_object.to_csv(new_file_name)
