"""Tests for the cleaning module"""
import pandas as pd
import life_expectancy.cleaning as cleaning

from . import OUTPUT_DIR


def test_clean_data(pt_life_expectancy_expected):
    """Run the main function and compare the output to the expected output"""
    cleaning.main()
    pt_life_expectancy_actual = pd.read_csv(
        OUTPUT_DIR / "pt_life_expectancy.csv"
    )
    pd.testing.assert_frame_equal(
        pt_life_expectancy_actual, pt_life_expectancy_expected
    )
