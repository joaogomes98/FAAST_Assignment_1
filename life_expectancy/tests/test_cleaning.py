"""Tests for the cleaning module"""
import pandas as pd
import life_expectancy.data_cleaning as dc
import life_expectancy.data_loading as dl
from life_expectancy.region import Region

def test_clean_data_tsv(eu_life_expectancy_raw_tsv: pd.DataFrame,
                        pt_life_expectancy_expected: pd.DataFrame) -> None:

    """
    Test for the clean_data function
    """
    dataloader = dl.LoaderPicker(dl.TsvLoader())
    dataframe = dataloader.normalize_df(eu_life_expectancy_raw_tsv)
    datacleaner = dc.DataCleaner(Region.PT)
    dataframe = datacleaner.clean_data(dataframe).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)

def test_clean_data_json(eurostat_life_expect_raw: pd.DataFrame,
                        pt_life_expectancy_expected: pd.DataFrame) -> None:

    """
    Test for the clean_data function
    """
    dataloader = dl.LoaderPicker(dl.JsonLoader())
    dataframe = dataloader.normalize_df(eurostat_life_expect_raw)
    datacleaner = dc.DataCleaner(Region.PT)
    dataframe = datacleaner.clean_data(dataframe).reset_index(drop=True)
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)
