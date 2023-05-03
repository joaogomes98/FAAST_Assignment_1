"""Tests for the main module"""
import pandas as pd
from unittest import mock
import life_expectancy.main as main
from . import OUTPUT_DIR
from life_expectancy.region import Region

EU_RAW_FILEPATH = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
PT_EXPECTANCY_FILEPATH = OUTPUT_DIR / "pt_life_expectancy.csv"


def test_main(pt_life_expectancy_expected):

    main_object = main.Main(EU_RAW_FILEPATH, PT_EXPECTANCY_FILEPATH, Region.PT)

    pt_life_expectancy_actual = main_object.main().reset_index(drop=True)

    pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)