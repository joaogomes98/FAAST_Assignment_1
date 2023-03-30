import logging
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

    return dataframe

def save_data(dataframe: pd.DataFrame, filepath: str) -> None:
    """
    Function responsible for saving the data to a file.
    """
    try:
        dataframe.to_csv(filepath, index=False)
    except PermissionError: #pragma: no cover
        logging.error("Permission denied: You do not have permission to write to the file.")
