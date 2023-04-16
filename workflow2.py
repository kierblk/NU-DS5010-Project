# Workflow 2:

# import package
From CleanlockHolmes import CleanlockHolmes

# Instatiate object
data_object = CleanlockHolmes("testcase.csv")

# run interactive mode for user to input specification
data_object.interactive_specify_col_data_types()

data_object.interactive_specify_viable_range()

# specify valid entries for food and color - all other entries considered invalid
data_object.specify_valid_entries(['sushi', 'pizza', 'other'] , 'Food')
data_object.specify_valid_entries(['red', 'blue', 'green'] , 'Color')

# identify invalid values and clean and export
invalid_values_tracker = data_object.identify_invalid_values()
    
data_object.clean_data(1, invalid_values_tracker, {'Food': 'not specified', 'Height' : 'out of range', 'Color': 'black', 'Weight' : 'out of range'})
    
data_object.write_data("cleaned_data.csv")
