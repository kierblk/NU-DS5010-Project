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

        return self.valid_dictionary

    def identify_invalid_values(self):

        """
        identifies row/col pairs that contain an invalid value 
        param None
        returns a list of indicies of corresponding to invalid data entries
        """
        rows , columns = self.data_object.shape
        invalid_values_tracker = np.zeros((rows - 1 , columns))
        print(invalid_values_tracker)

        for j in range(len(self.columns)):
            col = self.columns[j]
            for i in range(rows -1):
                if self.invalid_dictionary.get(col):
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

    output = data_object.specify_invalid_entries(['na', '', 'null', '0'], 'Height')

    #data_object.specify_invalid_entries([“NA”, “”, “null”, “--”], “Height”)
    #data_object.specify_invalid_entries([“NA”, “”, “null”, “--”, “0”], “Index”)


    data_object.specify_valid_entries(['male', 'female', 'other'] , 'Gender')
    data_object.specify_valid_entries(['red', 'blue', 'green'] , 'Color')
    

    output_3 = data_object.identify_invalid_values()
    # expect rows 2,3,4,57,8,9,10,11,12,13 to be dropped
    
    output_4 = data_object.clean_data(1, output_3, {'Gender': 'not specified', 'Height' : 'out of range', 'Color': 'Black'})
    print(output_4)

    data_object.write_data("cleaned_data.csv")

