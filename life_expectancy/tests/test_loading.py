"""Tests for the loading module"""
from unittest import mock
import pandas as pd
import life_expectancy.data_loading as dl
from . import FIXTURES_DIR, OUTPUT_DIR

def test_load_data_tsv(eu_life_expectancy_raw_csv: pd.DataFrame):

    """
    Test for the load_data function (tsv)
    """
    filepath = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
    dataloader = dl.LoaderPicker(dl.TsvLoader)
    dataframe = dataloader.load_df(filepath)
    pd.testing.assert_frame_equal(dataframe, eu_life_expectancy_raw_csv)

def test_load_data_json(eurostat_life_expect_raw: pd.DataFrame):

    """
    Test for the load_data function (json)
    """
    filepath = FIXTURES_DIR / "eurostat_life_expect.json"
    dataloader = dl.LoaderPicker(dl.JsonLoader)
    dataframe = dataloader.load_df(filepath)
    pd.testing.assert_frame_equal(dataframe, eurostat_life_expect_raw)

@mock.patch("life_expectancy.data_loading.pd.DataFrame.to_csv")
def test_save_data(mock_to_csv, pt_life_expectancy_expected: pd.DataFrame):

    """
    Test for the save_data function
    """
    filepath = OUTPUT_DIR / "pt_life_expectancy.csv"
    datasaver = dl.DataSaver()
    datasaver.save_data(pt_life_expectancy_expected, filepath)
    mock_to_csv.assert_called_with(filepath, index=False)
