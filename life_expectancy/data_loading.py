from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    """
    Abstract class for data loading and normalization.
    """

    @abstractmethod
    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Abstract method for loading the data.
        """

    @abstractmethod
    def normalize_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Abstract method for normalizing the data.
        """

class TsvLoader(DataLoader):
    """
    Concrete class for TSV data loading.
    """

    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Function responsible for loading the data.
        """
        dataframe = pd.read_csv(filepath, delimiter='\t')

        return dataframe

    def normalize_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Function responsible for normalizing the dataframe.
        """
        # Split the first column into separate columns
        dataframe[['unit', 'sex', 'age', 'region']] = dataframe['unit,sex,age,geo\\time']\
            .str.split(',', expand=True)

        # Drop the original composed column
        dataframe = dataframe.drop(columns=['unit,sex,age,geo\\time'])

        # Unpivot data to long format
        dataframe = dataframe.melt(id_vars=['unit','sex','age','region'], \
            var_name='year', value_name='value')

        return dataframe

class JsonLoader(DataLoader):
    """
    Concrete class for JSON data loading.
    """

    def load_data(self, filepath: str) -> pd.DataFrame:
        """
        Function responsible for loading the data.
        """
        dataframe = pd.read_json(filepath)

        return dataframe

    def normalize_data(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        # Drop columns "flag" and "flag_detail"
        dataframe = dataframe.drop(["flag", "flag_detail"], axis=1)

        # Rename columns "country" and "life_expectancy"
        dataframe = dataframe.rename(columns={"country": "region", "life_expectancy": "value"})

        # Select only the columns that we need
        dataframe = dataframe[["unit", "sex", "age", "region", "year", "value"]]

        return dataframe

class LoaderPicker:
    """
    Class responsible for executing the loader based on context.
    """

    def __init__(self, dataloader: DataLoader) -> None:
        self.dataloader = dataloader

    def load_df(self, filepath: str) -> pd.DataFrame:
        """
        Function responsible for calling load_data method
        """
        dataframe = self.dataloader.load_data(filepath)
        return dataframe

    def normalize_df(self, dataframe: pd.DataFrame) -> pd.DataFrame:
        """
        Function responsible for calling normalize_data method
        """
        dataframe = self.dataloader.normalize_data(dataframe)
        return dataframe

class DataSaver:
    """
    Class responsible for saving data to a file.
    """

    def save_data(self, dataframe: pd.DataFrame, filepath: str) -> None:
        """
        Function responsible for saving the data to a file.
        """
        dataframe.to_csv(filepath, index=False)
