import unittest
import pandas as pd
import numpy as np
from CleanlockHolmes import CleanlockHolmes

class TestCleanlockHolmes(unittest.TestCase):

    def setUp(self):
        '''
        Tests if CleanLockHolmes properly initializes by checking inputs
        '''
        self.cleanlockholmes = CleanlockHolmes('testcase.csv')

    def test_read_data_csv(self):
        '''
        Tests reading a given CSV file
        '''
        self.assertIsNotNone(self.cleanlockholmes.read_data('testcase.csv'))

    def test_read_data_json(self):
        '''
        Tests reading a given JSON file. This is expected to fail.
        '''
        self.cleanlockholmes = CleanlockHolmes('testcase.csv')
        self.assertIsNone(self.cleanlockholmes.read_data('testcase.json'))

    def test_specify_col_data_types(self):
        '''
        Tests if data type for given column is identified (user input)
        '''
        self.cleanlockholmes.specify_col_data_types('str', 'Food')
        self.assertEqual(self.cleanlockholmes.col_types_dictionary['Food'],['str'])

    def test_specify_invalid_entries(self):
        '''
        Tests output of given invalid entries for given column
        '''
        self.cleanlockholmes.specify_invalid_entries(['null'], 'Food')
        self.assertIn('null', self.cleanlockholmes.invalid_dictionary['Food'])

    def test_specify_valid_entries(self):
        '''
        Tests output of given valid entries for given column
        '''
        self.cleanlockholmes.specify_valid_entries(['green', 'blue'], 'Color')
        self.assertIn('green', self.cleanlockholmes.valid_dictionary['Color'])
        self.assertIn('blue', self.cleanlockholmes.valid_dictionary['Color'])
    
    def test_specify_viable_range(self):
        '''
        tests if upper and lower bounds are needed for a given column (user input)
        '''
        self.cleanlockholmes.specify_col_data_types('int', 'Height')
        self.cleanlockholmes.specify_viable_range(50, 125, 'Height')
        self.assertEqual(self.cleanlockholmes.data_ranges['Height'], [50.0, 125.0])

    def test_identify_invalid_values(self):
        '''
        Tests if given values are identified in table
        '''
        self.assertIn(1, self.cleanlockholmes.identify_invalid_values())

    def test_clean_data_method_1(self):
        '''
        Tests if cleaning value entries outputs based on method 1 of clean_data
        '''
        self.assertNotIn('null', self.cleanlockhomes._clean_data_row_drop(invalid_values_tracker = {'Food': ['null']}))

    def test_clean_data_method_2(self):
        '''
        Tests if cleaning value entries outputs based on method 2 of clean_data
        '''
        self.assertIn(['food'], self.cleanlockholmes._clean_data_replace_value(invalid_values_tracker = {'Food': ['null']}), {'Food': ['food']})


def main():
    unittest.main(verbosity=3)
main()