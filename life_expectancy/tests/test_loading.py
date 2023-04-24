"""Tests for the loading module"""
import pandas as pd
from unittest import mock
from life_expectancy.data_loading import load_data
from life_expectancy.data_loading import save_data
from . import FIXTURES_DIR, OUTPUT_DIR

def test_load_data(eu_life_expectancy_raw_csv):

    """Test for the load_data function"""
    filepath = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
    dataframe = load_data(filepath)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw_csv)


@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):

    """Test for the save_data function"""
    filepath = OUTPUT_DIR / "pt_life_expectancy.csv"
    save_data(pt_life_expectancy_expected, filepath)
    mock_to_csv.assert_called_with(filepath, index=False)
