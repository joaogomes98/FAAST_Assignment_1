import re
import pandas as pd
import numpy as np

def load_data(filepath: str) -> pd.DataFrame:
    """
    Function responsible for loading the data.
    """

    dataframe = pd.read_csv(filepath, delimiter='\t')

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

    # Convert year to int
    dataframe['year'] =  pd.to_numeric(dataframe['year'], errors='coerce').astype(int)

    # Apply the str_to_float method and perform data cleaning
    dataframe['value'] = dataframe['value'].apply(str_to_float)

    # Exclude all NaN values
    dataframe = dataframe.dropna(subset=['value'])

    # Filter by region
    dataframe = dataframe[dataframe['region'] == country]

    return dataframe

def save_data(dataframe: pd.DataFrame, filepath: str) -> None:
    """
    Function responsible for saving the data to a file.
    """

    dataframe.to_csv(filepath, index=False)

def str_to_float(val: str) -> float:
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

def main() -> None:
    """
    Main function responsible for executing the 3 steps -
    loading, cleaning and saving
    """

    dataframe = load_data('life_expectancy/data/eu_life_expectancy_raw.tsv')

    dataframe = clean_data(dataframe, 'PT')

    save_data(dataframe, 'life_expectancy/data/pt_life_expectancy.csv')


if __name__ == "__main__":  # pragma: no cover
    main()
