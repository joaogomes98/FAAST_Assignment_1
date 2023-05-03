import os
import pandas as pd
import life_expectancy.data_loading as dl
import life_expectancy.data_cleaning as dc
from life_expectancy.region import Region

class Main:
    """
    Main function responsible for executing the 3 steps -
    loading, cleaning and saving
    """

    def __init__(self, input_file: str, output_file: str, country: Region) -> None:
        self.input_file = input_file
        self.output_file = output_file
        self.country = country

    def get_file_extension(self) -> str:
        """
        Returns the extension of the file in the given path.
        """
        extension = os.path.splitext(self.input_file)
        return extension[1]

    def main(self) -> pd.DataFrame:
        """
        Main function responsible for executing the 3 steps -
        loading, cleaning and saving
        """

        file_format = self.get_file_extension()
        datasaver = dl.DataSaver()
        datacleaner = dc.DataCleaner(self.country)

        if file_format == ".json":
            dataloader = dl.LoaderPicker(dl.JsonLoader)
            dataframe = dataloader.load_df(self.input_file)
            dataframe = dataloader.normalize_df(dataframe)

        elif file_format == ".tsv":
            dataloader = dl.LoaderPicker(dl.TsvLoader)
            dataframe = dataloader.load_df(self.input_file)
            dataframe = dataloader.normalize_df(dataframe)

        dataframe = datacleaner.clean_data(dataframe)
        datasaver.save_data(dataframe, self.output_file)

        return dataframe
