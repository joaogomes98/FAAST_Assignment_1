"""Tests for the main module"""
import pandas as pd
from life_expectancy.main import main

def test_main(pt_life_expectancy_expected):

    """Test for the load_data function"""
    dataframe = main("PT")
    pd.testing.assert_frame_equal(dataframe, pt_life_expectancy_expected)
    