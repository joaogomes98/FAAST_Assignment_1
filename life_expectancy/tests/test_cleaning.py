"""Tests for the cleaning module"""
import pandas as pd
import life_expectancy.data_cleaning as dc
import life_expectancy.data_loading as dl
from life_expectancy.region import Region

def test_clean_data_tsv(eu_life_expectancy_raw_tsv, pt_life_expectancy_expected):

    """Test for the clean_data function"""
    dataLoader = dl.LoaderPicker(dl.TsvLoader)
    dataframe = dataLoader.normalize_df(eu_life_expectancy_raw_tsv)
    dataCleaner = dc.DataCleaner(Region.PT)
    dataframe = dataCleaner.clean_data(dataframe).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)

def test_clean_data_json(eurostat_life_expect_raw, pt_life_expectancy_expected):

    """Test for the clean_data function"""
    dataLoader = dl.LoaderPicker(dl.JsonLoader)
    dataframe = dataLoader.normalize_df(eurostat_life_expect_raw)
    dataCleaner = dc.DataCleaner(Region.PT)
    dataframe = dataCleaner.clean_data(dataframe).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)