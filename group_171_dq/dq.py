import great_expectations as gx
import pandas as pd
import json
import sys
import csv

# Import the necessary modules for experimental and custom expectations
from great_expectations.core import ExpectationSuite

# Set up hub for running our dq tool
context = gx.get_context()

# Identify delimiter that is used in csv file
def get_delimiter(file_path: str) -> str:
    with open(file_path, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter

#iterating through all csv files starting with first file at sys.argv[3]
arguments_from_start = sys.argv[3:]

#order of arguments passed to command line: json config file with expectations, output json file, file that we are 

#creating a validator object, which can house all of the expectations we want to run and use sys.argv[3] for its base file
#we also are passing a delimiter so that we know what is needed to parse the csv file

#storing delimiter in variable
delim_char = get_delimiter(sys.argv[3])

validator = context.sources.pandas_default.read_csv(sys.argv[3], sep=delim_char)


with open(sys.argv[1], 'r') as json_file:
    expectations_config = json.load(json_file) #loading json config file with expectations


df = pd.read_csv(sys.argv[3], sep=delim_char) #creating a dataframe for the currently selected file and accessing the delimiter to use to parse it
					     #this is better than creating a dataframe for each expectation, as that is memory intensive and expensive 
					     #rather, we are identifying which expectations have the same file path and adding those expectations to
					     #a list containing other expectations that would use the same dataframe
   

# Iterate through all expectations in the configuration file
for expectation in expectations_config.get("expectations", []): #access each of the expectations in the config file 

    expectation_type = expectation.get("expectation_type", "")  
									
    
    kwargs = expectation.get("kwargs", {})
    
    # Construct the Python code for loading an expectation into the validator object
    code = f"validator.{expectation_type}("
    code += ", ".join([f'{key}="{value}"' if isinstance(value, str) else f'{key}={value}' for key, value in kwargs.items()])
    code += ", result_format={'result_format': 'COMPLETE'}"
    code += ")"
    
    print(code)
    exec(code)
            
            

# Saves the expectations we added to our validator, and adds them to the expectation suite that
# exists within our context we created earlier (this expectation suite is different than the one
# that we have within our json config file, and the reason for translating to the context's expectation
# suite is that we want to have access to any experimental expectations that we want use
validator.save_expectation_suite()

# Runs the expectations against our csv data
output = validator.validate()

# Converts the output to a json dictionary format
validation_result_dict = output.to_json_dict()

# Serialize the dictionary to JSON with indentation
json_object = json.dumps(validation_result_dict, indent=4)

# Save the JSON data to a file
with open(sys.argv[2], "w") as outfile:
    outfile.write(json_object)

