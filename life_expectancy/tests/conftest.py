"""Pytest configuration file"""
import pandas as pd
import pytest
from pathlib import Path
from life_expectancy.data_cleaning import clean_data
from life_expectancy.data_loading import load_data
from life_expectancy.data_loading import save_data

from . import FIXTURES_DIR, OUTPUT_DIR

DATA_DIR = "life_expectancy/data"

@pytest.fixture(autouse=True)
def run_before_and_after_tests() -> None:
    """Fixture to execute commands before and after a test is run"""
    # Setup: fill with any logic you want

    yield # this is where the testing happens

    # Teardown : fill with any logic you want
    file_path = OUTPUT_DIR / "pt_life_expectancy.csv"
    file_path.unlink(missing_ok=True)
    
@pytest.fixture(scope="session")
def eu_life_expectancy_raw_tsv() -> pd.DataFrame:

    """Fixture to load the raw life expectancy data"""
    filepath = FIXTURES_DIR / "eu_life_expectancy_raw.tsv"
    return pd.read_csv(filepath, delimiter='\t')

@pytest.fixture(scope="session")
def eu_life_expectancy_raw_csv() -> pd.DataFrame:

    """Fixture to load the raw life expectancy data"""
    return pd.read_csv(FIXTURES_DIR / "eu_life_expectancy_raw.csv")

@pytest.fixture(scope="session")
def pt_life_expectancy_expected() -> pd.DataFrame:
    
    """Fixture to load the expected output"""
    return pd.read_csv(FIXTURES_DIR / "pt_life_expectancy_expected.csv")