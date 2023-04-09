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


    def specify_col_data_types(self):
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

        print(df.columns)
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



        return self.invalid_dictionary
            

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
        

    def specify_viable_range(self):
        """
        Specifies a viable column range of values where col is
        specified numeric 
        param None
        return
        """
        for column in self.columns:
            if self.col_types_dictionary[column] == ['int'] or self.col_types_dictionary[column] == ['float']:
                min_value = None
                max_value = None
                while type(min_value) != int or type(max_value) != int:
                    try:
                        min_value = int(input(f"Please enter an integer lower bound for {column}: "))
                        max_value = int(input(f"Please enter an integer upper bound for {column}: "))

                    except:
                        print("only numeric values accepted")
                        min_value = int(input(f"Please enter an integer lower bound for {column}: "))
                        max_value = int(input(f"Please enter an integer upper bound for {column}: "))
                
     
                self.data_ranges[column] = [int(min_value), int(max_value)]

        return self.data_ranges


    def identify_invalid_values(self):

        """
        identifies row/col pairs that contain an invalid value 
        param None
        returns None
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
                    elif self.data_object.loc[i].at[col] < self.data_ranges[col][0] or self.data_object.loc[i].at[col] > self.data_ranges[col][1]:
                        invalid_values_tracker[i][j] =1               
                elif self.invalid_dictionary.get(col):
                    if self.data_object.loc[i].at[col] in self.invalid_dictionary[col]:
                        invalid_values_tracker[i][j] = 1
                elif self.valid_dictionary.get(col):
                    if self.data_object.loc[i].at[col] not in self.valid_dictionary[col]:
                        invalid_values_tracker[i][j] = 1
        print(invalid_values_tracker)          
        return invalid_values_tracker
                

    def clean_data(self, method, invalid_values_tracker, arg = {}):

        """
        Function utilizes chosen method to rectify problematic value entries.
        Selects a method from these options:
        method 1 drop_row: removes data point
        method 2 replace_row : replaces problematic data point with values
        method 3 replace_average : replaces problematic numeric data point with the median and mode for categorical
        specified in arg["replacement"]
        param

                method - rectification method specified by user
                arg - dictionary containg replacement options
        returns None

        """
        rows, columns = invalid_values_tracker.shape
        if method == 1:
            for i in range(rows):
                total = sum(invalid_values_tracker[i])
                if total > 0:
                    self.data_object = self.data_object.drop([i])

        elif method == 2:
            for i in range(rows):
                for j in range(columns):
                    col = self.columns[j]
                    if invalid_values_tracker[i][j] == 1:
                        self.data_object.loc[i].at[col] = arg[col]

        elif method == 3:
            for i in range(rows):
                for j in range(columns):
                    col = self.columns[j]
                        
                    if invalid_values_tracker[i][j] == 1:
                        try:
                            col_median = self.data_object[col].median()
                            print(col_median)
                            self.data_object.loc[i].at[col] = col_median

                        except TypeError:
                            col_mode = self.data_object[col].mode()
                            print(col_mode)
                            self.data_object.loc[i].at[col] = col_mode

        return self.data_object

        
          
            

    def write_data(self, new_file_name):

        """
        Function writes rectified data to a specified file
        param new_file_name: specified file
        returns None
        """

        self.data_object.to_csv(new_file_name)
                

        
if __name__ == "__main__":

    data_object = CleanlockHolmes("testcase.csv")
    print(data_object.data_object)

    data_object.specify_col_data_types()

    output_2 = data_object.specify_viable_range()
    print(output_2["Height"][0])
    print(output_2['Height'][0])
    
 
    
    
    # output = data_object.specify_invalid_entries(['na', '', 'null', '0'], 'Height')
    # output = data_object.specify_invalid_entries(['na', '', 'null', '0'], 'Weight')


    data_object.specify_valid_entries(['sushi', 'pizza', 'other'] , 'Food')
    data_object.specify_valid_entries(['red', 'blue', 'green'] , 'Color')
    
    

    output_3 = data_object.identify_invalid_values()
    print(output_3)
    
    output_4 = data_object.clean_data(1, output_3, {'Food': 'not specified', 'Height' : 'out of range', 'Color': 'black'})
    print(output_4)

    data_object.write_data("cleaned_data.csv")

    
    

