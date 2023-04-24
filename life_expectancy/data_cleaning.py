import pandas as pd

def clean_data(dataframe: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Function responsible for cleaning the data and 
    filtering it according to a specific region.

    The data cleaning follows this logic: the years are converted 
    into integers and the values are converted into floats
    """
    # Split the first column into separate columns
    dataframe[['unit', 'sex', 'age', 'region']] = dataframe['unit,sex,age,geo\\time']\
        .str.split(',', expand=True)

    # Drop the original composed column
    dataframe = dataframe.drop(columns=['unit,sex,age,geo\\time'])

    # Unpivot data to long format
    dataframe = dataframe.melt(id_vars=['unit','sex','age','region'], \
        var_name='year', value_name='value')

    # Specify data types for the unit, sex, age and region columns
    dtypes = {'unit': str, 'sex': str, 'age': str, 'region': str}

    dataframe = dataframe.astype(dtypes)

    # Convert year column to int
    dataframe['year'] =  pd.to_numeric(dataframe['year'], errors='coerce').astype('int64')

    # Convert the value column to floats or NaNs, using regex
    dataframe["value"] = dataframe["value"].str.replace(r"[^0-9.]+", "", regex=True)
    dataframe["value"] = pd.to_numeric(dataframe["value"], errors="coerce")

    # Exclude all NaN values
    dataframe = dataframe.dropna(subset=['value', 'year'])

    # Filter by region
    dataframe = dataframe[dataframe['region'] == country]

    return dataframe
