"""Tests for the main module"""
import pandas as pd
from unittest import mock
from life_expectancy.main import main
from . import OUTPUT_DIR

EU_RAW_FILEPATH = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
PT_EXPECTANCY_FILEPATH = OUTPUT_DIR / "pt_life_expectancy.csv"

@mock.patch("life_expectancy.main.load_data")
@mock.patch("life_expectancy.main.clean_data")
@mock.patch("life_expectancy.main.save_data")
def test_main(mock_save_data,
    mock_clean_data,
    mock_load_data,
    pt_life_expectancy_expected,
    eu_life_expectancy_raw_csv):

    """ Test for main module """
    mock_load_data.return_value = eu_life_expectancy_raw_csv
    mock_clean_data.return_value = pt_life_expectancy_expected

    pt_life_expectancy_actual = main("PT")

    mock_load_data.assert_called_once_with(EU_RAW_FILEPATH)
    mock_clean_data.assert_called_once_with(eu_life_expectancy_raw_csv, "PT")
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, PT_EXPECTANCY_FILEPATH)

    pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)