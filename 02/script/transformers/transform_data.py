import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    print(f"total data before transform: {len(data)}")
    data = data.query("passenger_count > 0 and trip_distance > 0")

    print("Data Type Before Conversion")
    print(data.dtypes)

    # rename column to snake case
    new_data_columns = dict()
    for col in data.columns:
        new_col = col.replace("ID", "Id").replace("PU", "Pu").replace("DO", "Do")
        new_col = camel_to_snake(new_col)
        new_data_columns[col] = new_col
    
    data.rename(columns=new_data_columns, inplace=True)


    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    print("Data Type After Conversion")
    print(data.dtypes)
    print(f"total data after transform: {len(data)}")
    return data


def camel_to_snake(camel_case_string):
   snake_case_string = ""
   for i, c in enumerate(camel_case_string):
      if i == 0:
         snake_case_string += c.lower()
      elif c.isupper():
         snake_case_string += "_" + c.lower()
      else:
         snake_case_string += c

   return snake_case_string

@test
def test_vendor_id(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert (output['vendor_id'] == 1).any(), 'Data vendor_id is not valid'

@test
def test_passanger_count(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert not (output['passenger_count'] == 0).any(), 'Any data passanger_count = 0'

@test
def test_trip_distance(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert not (output['trip_distance'] == 0).any(), 'Any data trip_distance = 0'