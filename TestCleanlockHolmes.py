import unittest
import pandas as pd
import numpy as np
from CleanlockHolmes import CleanlockHolmes

class TestCleanlockHolmes(unittest.TestCase):

# for the following tests --> self.assertEqual; self.assertTrue

    def test_init(self):
        '''
        Tests if CleanLockHolmes properly initializes by checking inputs
        '''
        self.filename = 'testcase.csv'
        self.CleanlockHolmes = CleanlockHolmes(self.filename)

    def test_read_data(self):
        '''
        Tests reading a given file
        *still in progress
        '''
        table = {'col1': ['a', 'b', 'c'], 'col2': [1, 2, 3], 'col3': [4, 5, 6]}
        expected_output = pd.DataFrame(table)
        self.assertEqual(self.CleanlockHolmes.data_object.equals(expected_output), True)

    def test_specify_invalid_entries(self):
        '''
        Tests if entries are invalid for given column
        '''
        invalid_values = ['a','b','c']
        col = 'col1'
        self.CleanlockHolmes.specify_invalid_entries(invalid_values, col)
        expected_invalid_dict = {'col1': ['b']}
        self.assertDictEqual(self.CleanlockHolmes.invalid_dictionary, expected_invalid_dict)

    def test_specify_valid_entries(self):
        '''
        test
        '''
        valid_values = ['a','b','c']
        col = 'col1'
        self.CleanlockHolmes.specify_valid_entries(valid_values, col)
        expected_valid_dict = {'col1': ['a','b','c']}
        self.assertDictEqual(self.CleanlockHolmes.valid_dictionary, expected_valid_dict)

    def test_identify_invalid_values(self):
        '''
        test
        '''
        pass

    def test_clean_data(self):
        '''
        test
        '''
        pass

    def test_write_data(self):
        '''
        test
        '''
        pass


def main():
    unittest.main(verbosity=3)
main()