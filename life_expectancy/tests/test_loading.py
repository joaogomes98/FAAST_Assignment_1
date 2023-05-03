"""Tests for the loading module"""
import pandas as pd
from unittest import mock
import life_expectancy.data_loading as dl
from . import FIXTURES_DIR, OUTPUT_DIR

def test_load_data_tsv(eu_life_expectancy_raw_csv):

    """Test for the load_data function"""
    filepath = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
    dataLoader = dl.LoaderPicker(dl.TsvLoader)
    dataframe = dataLoader.load_df(filepath)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw_csv)

def test_load_data_json(eurostat_life_expect_raw):

    filepath = FIXTURES_DIR / "eurostat_life_expect.json"
    dataLoader = dl.LoaderPicker(dl.JsonLoader)
    dataframe = dataLoader.load_df(filepath)
    pd.testing.assert_frame_equal(dataframe, eurostat_life_expect_raw)

@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected):

    """Test for the save_data function"""
    filepath = OUTPUT_DIR / "pt_life_expectancy.csv"
    dataSaver = dl.DataSaver()
    dataSaver.save_data(pt_life_expectancy_expected, filepath)
    mock_to_csv.assert_called_with(filepath, index=False)
