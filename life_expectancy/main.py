import argparse
from pathlib import Path
import pandas as pd
import life_expectancy.data_loading as dl
import life_expectancy.data_cleaning as dc
from life_expectancy.region import Region


DEFAULT_INPUT_FILE = "life_expectancy/data/eu_life_expectancy_raw.tsv"
DEFAULT_OUTPUT_FILE = "life_expectancy/output/pt_life_expectancy.csv"

def get_file_extension(input_file: str) -> str:
    """
    Returns the extension of the file in the given path.
    """
    path = Path(input_file)
    return path.suffix


def main(input_file: str, output_file: str, country: Region) -> pd.DataFrame:
    """
    Main function responsible for executing the 3 steps -
    loading, cleaning and saving
    """

    file_format = get_file_extension(input_file)
    datasaver = dl.DataSaver()
    datacleaner = dc.DataCleaner(country)

    if file_format == ".json":
        dataloader = dl.LoaderPicker(dl.JsonLoader)

    elif file_format == ".tsv":
        dataloader = dl.LoaderPicker(dl.TsvLoader)

    dataframe = dataloader.load_df(input_file)
    dataframe = dataloader.normalize_df(dataframe)
    dataframe = datacleaner.clean_data(dataframe)
    datasaver.save_data(dataframe, output_file)

    return dataframe

if __name__ == "__main__":  # pragma: no cover

    # Create argument parser
    parser = argparse.ArgumentParser(description='Clean life expectancy \
        data for a specified country')
    parser.add_argument('--input_file', type=str, default= DEFAULT_INPUT_FILE,
                        help='Path to input file')
    parser.add_argument('--output_file', type=str, default= DEFAULT_OUTPUT_FILE,
                        help='Path to output file')
    parser.add_argument('--country', type=Region, default=Region.PT, help='ISO code \
        of country to filter by')

    # Parse arguments
    args = parser.parse_args()

    # Call clean_data with specified country
    main(args.input_file, args.output_file, args.country)
