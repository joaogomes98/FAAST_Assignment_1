import argparse
from pathlib import Path
from life_expectancy.data_loading import load_data
from life_expectancy.data_loading import save_data
from life_expectancy.data_cleaning import clean_data

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
    
    dataframe = dataframe.reset_index(drop=True)

    return dataframe


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