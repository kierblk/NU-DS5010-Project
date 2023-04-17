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

    def test_read_data_csv(self):
        '''
        Tests reading a given CSV file
        '''
        self.assertIsNotNone(self.CleanlockHolmes.read_data('data.csv'))

    def test_read_data_json(self):
        '''
        Tests reading a given JSON file
        '''
        self.assertIsNotNone(self.CleanlockHolmes.read_data('data.json'))

    def test_read_data_json(self):
        '''
        Tests reading a given an file that is not supported
        '''
        self.assertIsNotNone(self.CleanlockHolmes.read_data('data.txt')) 

    def test_interactive_specify_col_data_types(self):
        '''
        Tests if data type for given column is identified (prompt user)
        '''
        self.CleanlockHolmes.interactive_specify_col_data_types('str', 'col1')
        self.assertEqual(self.CleanlockHolmes.col_types_dictionary['col1', ['str']])

    def test_specify_col_data_types(self):
        '''
        Tests if data type for given column is identified (user input)
        '''
        self.CleanlockHolmes.specify_col_data_types('int', 'col1')
        self.assertEqual(self.CleanlockHolmes.col_types_dictionary['col1', ['int']])

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
        tests if upper and lower bounds are needed for a given column (prompt user)
        '''
        self.CleanlockHolmes.specify_col_data_types()
        self.CleanlockHolmes.interactive_specify_viable_range()
        expected_range = {'col1': [20, 300], 'col2': [5, 20]}
        self.assertDictEqual(self.CleanlockHolmes.data_ranges, expected_range)
    
    def test_specify_viable_range(self):
        '''
        tests if upper and lower bounds are needed for a given column (user input)
        '''
        self.CleanlockHolmes.specify_col_data_types('int', 'col1')
        self.CleanlockHolmes.specify_viable_range(100, 200, 'col1')
        self.assertEqual(self.CleanlockHolmes.data_ranges['col1', [100, 200]])

    def test_identify_invalid_values(self):
        '''
        Tests if given values are identified in table
        '''
        self.CleanlockHolmes.specify_col_data_types()
        self.CleanlockHolmes.specify_invalid_entries(['a'], 'col1')
        self.CleanlockHolmes.specify_viable_range()
        invalid_test = self.CleanlockHolmes.identify_invalid_values()
        expected_test = ''
        self.assertEqual(self.CleanlockHolmes.invalid_dictionary['col1', ['a']])

    def test_clean_data(self):
        '''
        Tests if cleaning value entries outputs based on chosen method
        '''
        pass


    def main():
        unittest.main(verbosity=3)
    main()