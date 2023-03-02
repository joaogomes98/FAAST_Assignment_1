import re
import argparse
import pandas as pd
import numpy as np

def clean_data(country):
    """
    Function responsible for loading the data, cleaning it and 
    filtering it according to a specific region.

    The data cleaning follows this logic: the years are converted 
    into integers and the values are converted into floats
    """

    # Load data
    dataframe = pd.read_csv('life_expectancy/data/eu_life_expectancy_raw.tsv', delimiter='\t')

    # Split the first column into separate columns
    dataframe[['unit', 'sex', 'age', 'region']] = dataframe['unit,sex,age,geo\\time']\
        .str.split(',', expand=True)

    # Drop the original composed column
    dataframe = dataframe.drop(columns=['unit,sex,age,geo\\time'])

    # Unpivot data to long format
    dataframe = dataframe.melt(id_vars=['unit','sex','age','region'], \
        var_name='year', value_name='value')

    # Convert year to int
    dataframe['year'] =  pd.to_numeric(dataframe['year'], errors='coerce').astype(int)

    # Apply the str_to_float method and perform data cleaning
    dataframe['value'] = dataframe['value'].apply(str_to_float)

    # Exclude all NaN values
    dataframe = dataframe.dropna(subset=['value'])

    # Filter by region = PT
    dataframe = dataframe[dataframe['region'] == country]

    # Save cleaned data to csv
    dataframe.to_csv('life_expectancy/data/pt_life_expectancy.csv', index=False)

def str_to_float(val):
    """
    A helper function to convert a string value to a float number, 
    or NaN (Not a Number) if the conversion is not possible.

    If the input string has letters, they will be removed first.
    """
    try:
        # Try to convert the value to a float number
        num = float(re.search(r'\d+\.*\d*', val).group(0))
        return num
    except (ValueError, AttributeError):
        # If the conversion fails, return NaN
        return np.nan

if __name__ == "__main__":  # pragma: no cover

     # Create argument parser
    parser = argparse.ArgumentParser(description='Clean life expectancy \
        data for a specified country')
    parser.add_argument('--country', type=str, default='PT', help='ISO code \
        of country to filter by')

    # Parse arguments
    args = parser.parse_args()

    # Call clean_data with specified country
    clean_data(args.country)
