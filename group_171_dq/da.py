import great_expectations as gx
import sys
import json
from great_expectations.core.batch import BatchRequest
from great_expectations.core.yaml_handler import YAMLHandler
from great_expectations.datasource.fluent.interfaces import DataAsset
import csv
import pandas as pd

yaml = YAMLHandler()
context = gx.get_context()


def get_delimiter(file_path: str) -> str:
    with open(file_path, 'r') as csvfile:
        delimiter = str(csv.Sniffer().sniff(csvfile.read()).delimiter)
        return delimiter

delim = get_delimiter(sys.argv[1])


datasource = context.sources.add_pandas(name="my_pandas_datasource")
dataframe = pd.read_csv(sys.argv[1],sep=delim)
#dataframe = pd.read_csv(sys.argv[1])


name = "taxi_dataframe"

data_asset = datasource.add_dataframe_asset(name=name)

my_batch_request = data_asset.build_batch_request(dataframe=dataframe)


expectation_suite_name = "ry_assistant_suite"

expectation_suite = context.add_or_update_expectation_suite(
    expectation_suite_name=expectation_suite_name
)


exclude_column_names =[]
data_assistant_result = context.assistants.onboarding.run(
    batch_request=my_batch_request,
    exclude_column_names=exclude_column_names,
)
output_file_path = sys.argv[2]

with open(output_file_path, 'w') as output_file:
    json.dump(data_assistant_result.get_expectation_suite().to_json_dict(), output_file, indent=4)

