"""Tests for the main module"""
import pandas as pd
from unittest import mock
from life_expectancy.main import main
from . import OUTPUT_DIR, FIXTURES_DIR
from life_expectancy.region import Region

EU_RAW_FILEPATH_CSV = OUTPUT_DIR / "eu_life_expectancy_raw.tsv"
EUROSTAT_EXPECTANCY_FILEPATH_JSON = OUTPUT_DIR / "eurostat_life_expected.json"
PT_EXPECTANCY_FILEPATH = OUTPUT_DIR / "pt_life_expectancy.csv"
EUROSTAT_EXPECTANCY_FILEPATH = FIXTURES_DIR / "eurostat_life_expectancy_expected.csv"

@mock.patch('life_expectancy.data_cleaning.DataCleaner.clean_data')
@mock.patch('life_expectancy.data_loading.LoaderPicker.load_df')
@mock.patch('life_expectancy.data_loading.DataSaver.save_data')
def test_main_csv(mock_load_df, 
                mock_save_data, 
                mock_clean_data,
                pt_life_expectancy_expected,
                eu_life_expectancy_raw_csv):

    mock_load_df.return_value = eu_life_expectancy_raw_csv
    mock_clean_data.return_value = pt_life_expectancy_expected

    pt_life_expectancy_actual = main(EU_RAW_FILEPATH_CSV, 
                                     PT_EXPECTANCY_FILEPATH, 
                                     Region.PT)
    
    '''
    mock_load_df.assert_called_once_with(mock.ANY, EU_RAW_FILEPATH_CSV)
    mock_clean_data.assert_called_once_with(mock.ANY, Region.PT)
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, PT_EXPECTANCY_FILEPATH)
    '''

    pd.testing.assert_frame_equal(pt_life_expectancy_actual, pt_life_expectancy_expected)

@mock.patch('life_expectancy.data_cleaning.DataCleaner.clean_data')
@mock.patch('life_expectancy.data_loading.LoaderPicker.load_df')
@mock.patch('life_expectancy.data_loading.DataSaver.save_data')
def test_main_json(mock_load_df, 
                mock_save_data, 
                mock_clean_data,
                eurostat_life_expectancy_expected,
                eurostat_life_expect_raw):

    mock_load_df.return_value = eurostat_life_expect_raw
    mock_clean_data.return_value = eurostat_life_expectancy_expected

    eurostat_life_expectancy_actual = main(EUROSTAT_EXPECTANCY_FILEPATH_JSON, 
                                     EUROSTAT_EXPECTANCY_FILEPATH, 
                                     Region.PT)
    
    '''
    mock_load_df.assert_called_once_with(mock.ANY, EU_RAW_FILEPATH_CSV)
    mock_clean_data.assert_called_once_with(mock.ANY, Region.PT)
    mock_save_data.assert_called_once_with(pt_life_expectancy_expected, PT_EXPECTANCY_FILEPATH)
    '''

    pd.testing.assert_frame_equal(eurostat_life_expectancy_actual, eurostat_life_expectancy_expected)