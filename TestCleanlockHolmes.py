import unittest
import pandas as pd
import numpy as np
from CleanlockHolmes import CleanlockHolmes

class TestCleanlockHolmes(unittest.TestCase):


    def test_init(self):
        '''
        Tests if CleanLockHolmes properly initializes by checking inputs
        '''
        self.filename = 'testcase.csv'
        self.CleanlockHolmes = CleanlockHolmes(self.filename)

    def test_interactive_specify_col_data_types(self):
        '''
        PLACEHOLDER: in the event interactive is used instead of other version
        '''
        pass

    def test_specify_col_data_types(self):
        '''
        Tests if data type for given column is identified
        '''
        pass

    def test_read_data(self):
        '''
        Tests reading a given file
        '''
        table = {'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3], 'col3': [4, 5, 6]}
        expected_output = pd.DataFrame(table)
        self.assertEqual(self.CleanlockHolmes.data_object.equals(expected_output), True)

    def test_specify_invalid_entries(self):
        '''
        Tests output of given invalid entries for given column
        '''
        invalid_values = ['a','b','c']
        col = 'col1'
        self.CleanlockHolmes.specify_invalid_entries(invalid_values, col)
        expected_invalid_dict = {'col1': ['b']}
        self.assertDictEqual(self.CleanlockHolmes.invalid_dictionary, expected_invalid_dict)

    def test_specify_valid_entries(self):
        '''
        Tests output of given valid entries for given column
        '''
        valid_values = ['a','b','c']
        col = 'col1'
        self.CleanlockHolmes.specify_valid_entries(valid_values, col)
        expected_valid_dict = {'col1': ['a','b','c']}
        self.assertDictEqual(self.CleanlockHolmes.valid_dictionary, expected_valid_dict)

    def test_interactive_specify_viable_range(self):
        '''
        PLACEHOLDER: in the event interactive is used instead of other version
        '''
        pass
    
    def test_specify_viable_range(self):
        '''
        tests if upper and lower bounds are needed for a given column
        '''
        self.CleanlockHolmes.specify_col_data_types()
        self.CleanlockHolmes.specify_viable_range()
        expected_range = {'col1': [20, 300], 'col2': [5, 20]}
        self.assertDictEqual(self.CleanlockHolmes.data_ranges, expected_range)

    def test_identify_invalid_values(self):
        '''
        Tests if given values are identified in table
        '''
        pass

    def test_clean_data(self):
        '''
        Tests if cleaning value entries outputs based on chosen method
        '''
        pass

    def test_write_data(self):
        '''
        Tests if file is written to cvs or json file
        '''
        pass


def main():
    unittest.main(verbosity=3)
main()