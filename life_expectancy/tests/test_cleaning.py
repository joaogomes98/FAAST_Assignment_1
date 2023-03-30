"""Tests for the cleaning module"""
import pandas as pd
from unittest import mock
import life_expectancy.main as main
from life_expectancy.data_loading import load_data
from life_expectancy.data_loading import save_data
from life_expectancy.data_cleaning import clean_data

from . import OUTPUT_DIR

def test_main(pt_life_expectancy_expected):

    """Run the main function and compare the output to the expected output"""
    dataframe = main.main("PT")
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)

def test_load_data(eu_life_expectancy_raw):

    """Test for the load_data function"""
    filepath = "life_expectancy/data/eu_life_expectancy_raw.tsv"
    dataframe = load_data(filepath).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw)


def test_clean_data(eu_life_expectancy_raw, pt_life_expectancy_expected):

    """Test for the clean_data function"""
    dataframe = clean_data(eu_life_expectancy_raw, "PT").reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)

@mock.patch("pandas.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_raw):

    """Test for the save_data function"""
    filepath = "life_expectancy/data/pt_life_expectancy.csv"
    save_data(pt_life_expectancy_raw, filepath)
    mock_to_csv.assert_called_with(filepath, index=False)
