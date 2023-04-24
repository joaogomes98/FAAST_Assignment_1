import pandas as pd

def load_data(filepath: str) -> pd.DataFrame:
    """
    Function responsible for loading the data.
    """
    dataframe = pd.read_csv(filepath, delimiter='\t')

    return dataframe

def save_data(dataframe: pd.DataFrame, filepath: str) -> None:
    """
    Function responsible for saving the data to a file.
    """
    dataframe.to_csv(filepath, index=False)
