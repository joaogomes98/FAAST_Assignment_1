import pandas as pd
from life_expectancy.region import Region

class DataCleaner:
    """
    Class responsible for cleaning data from a dataframe.
    """
    def __init__(self, country: Region) -> None:
        self.country = country.value

    def clean_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Function responsible for cleaning the data and 
        filtering it according to a specific region.

        The data cleaning follows this logic: the years are converted 
        into integers and the values are converted into floats
        """

        # Specify data types for the unit, sex, age and region columns
        dtypes = {'unit': str, 'sex': str, 'age': str, 'region': str, 'value': str}

        dataframe = dataframe.astype(dtypes)

        # Convert year column to int
        dataframe['year'] =  pd.to_numeric(dataframe['year'], errors='coerce').astype('int64')

        # Convert the value column to floats or NaNs, using regex
        dataframe["value"] = dataframe["value"].str.replace(r"[^0-9.]+", "", regex=True)
        dataframe["value"] = pd.to_numeric(dataframe["value"], errors="coerce")

        # Exclude all NaN values
        dataframe = dataframe.dropna(subset=['value', 'year'])

        # Filter by region
        dataframe = dataframe[dataframe['region'] == self.country]

        return dataframe
