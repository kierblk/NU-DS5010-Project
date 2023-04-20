# Workflow 1:

# import package
from CleanlockHolmes import CleanlockHolmes

# Instatiate object
data_object = CleanlockHolmes("testcase.csv")

# specify invalid values for weight and height- all other entries considered valid
data_object.specify_invalid_entries(['NA', '', 'null', '--'], 'Weight')
data_object.specify_invalid_entries(['NA', '', 'null', '--'], 'Height')

# specify valid entries for food and color - all other entries considered invalid
data_object.specify_valid_entries(['sushi', 'pizza', 'other'] , 'Food')
data_object.specify_valid_entries(['red', 'blue', 'green'] , 'Color')

# identify invalid values and clean and export
invalid_values_tracker = data_object.identify_invalid_values()
    
data_object.clean_data(3, invalid_values_tracker, {'Food': 'not specified', 'Height' : 'out of range', 'Color': 'black', 'Weight' : 'out of range'})
    
data_object.write_data("cleaned_data.csv")

    
    
