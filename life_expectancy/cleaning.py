import argparse
import logging
from pathlib import Path
import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Function responsible for loading the data.
    """
    try:
        dataframe = pd.read_csv(filepath, delimiter='\t')
    except FileNotFoundError: #pragma: no cover
        logging.error("File not found: The specified file does not exist.")
    except PermissionError: #pragma: no cover
        logging.error("Permission denied: You do not have permission to read the file.")

    # Split the first column into separate columns
    dataframe[['unit', 'sex', 'age', 'region']] = dataframe['unit,sex,age,geo\\time']\
        .str.split(',', expand=True)

    # Drop the original composed column
    dataframe = dataframe.drop(columns=['unit,sex,age,geo\\time'])

    # Unpivot data to long format
    dataframe = dataframe.melt(id_vars=['unit','sex','age','region'], \
        var_name='year', value_name='value')

    return dataframe

def clean_data(dataframe: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Function responsible for cleaning the data and 
    filtering it according to a specific region.

    The data cleaning follows this logic: the years are converted 
    into integers and the values are converted into floats
    """

    # Specify data types for the unit, sex, age and region columns
    dtypes = {'unit': str, 'sex': str, 'age': str, 'region': str}

    dataframe = dataframe.astype(dtypes)

    # Convert year column to int
    dataframe['year'] =  pd.to_numeric(dataframe['year'], errors='coerce').astype(int)

    # Convert the value column to floats or NaNs, using regex
    dataframe["value"] = dataframe["value"].str.replace(r"[^0-9.]+", "", regex=True)
    dataframe["value"] = pd.to_numeric(dataframe["value"], errors="coerce")

    # Exclude all NaN values
    dataframe = dataframe.dropna(subset=['value', 'year'])

    # Filter by region
    dataframe = dataframe[dataframe['region'] == country]

    return dataframe

def save_data(dataframe: pd.DataFrame, filepath: str) -> None:
    """
    Function responsible for saving the data to a file.
    """
    try:
        dataframe.to_csv(filepath, index=False)
    except PermissionError: #pragma: no cover
        logging.error("Permission denied: You do not have permission to write to the file.")

def main(country: str) -> None:
    """
    Main function responsible for executing the 3 steps -
    loading, cleaning and saving
    """

    filepath = Path(__file__).resolve()
    basepath = filepath.parent

    input_filepath = basepath/'data'/'eu_life_expectancy_raw.tsv'
    output_filepath = basepath/'data'/'pt_life_expectancy.csv'

    dataframe = load_data(input_filepath)

    dataframe = clean_data(dataframe, country)

    save_data(dataframe, output_filepath)


if __name__ == "__main__":  # pragma: no cover

    # Create argument parser
    parser = argparse.ArgumentParser(description='Clean life expectancy \
        data for a specified country')
    parser.add_argument('--country', type=str, default='PT', help='ISO code \
        of country to filter by')

    # Parse arguments
    args = parser.parse_args()

    # Call clean_data with specified country
    main(args.country)
