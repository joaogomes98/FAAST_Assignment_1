"""Tests for the main module"""
import pandas as pd
from life_expectancy.main import main
from life_expectancy.region import Region
from . import OUTPUT_DIR, FIXTURES_DIR

EU_RAW_FILEPATH_CSV = str(OUTPUT_DIR / "eu_life_expectancy_raw.tsv")
EUROSTAT_EXPECTANCY_FILEPATH_JSON = str(OUTPUT_DIR / "eurostat_life_expect.json")
PT_EXPECTANCY_FILEPATH = str(OUTPUT_DIR / "pt_life_expectancy.csv")
EUROSTAT_EXPECTANCY_FILEPATH = str(FIXTURES_DIR / "eurostat_life_expectancy_expected.csv")

def test_main_csv(pt_life_expectancy_expected: pd.DataFrame) -> None:
    """
    Function to test the main module (csv)
    """

    pt_life_expectancy_actual = main(EU_RAW_FILEPATH_CSV,
                                     PT_EXPECTANCY_FILEPATH,
                                     Region.PT).reset_index(drop=True)

    pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)

def test_main_json(eurostat_life_expectancy_expected: pd.DataFrame) -> None:

    """
    Function to test the main module (csv)
    """
    eurostat_life_expectancy_actual = main(EUROSTAT_EXPECTANCY_FILEPATH_JSON,
                                     EUROSTAT_EXPECTANCY_FILEPATH,
                                     Region.PT).reset_index(drop=True)

    pd.testing.assert_frame_equal(eurostat_life_expectancy_actual,
                                eurostat_life_expectancy_expected)
