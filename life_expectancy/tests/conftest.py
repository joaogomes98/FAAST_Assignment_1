"""Pytest configuration file"""
import pandas as pd
import pytest

from . import FIXTURES_DIR, OUTPUT_DIR

DATA_DIR = "life_expectancy/data"
ALL_COUNTRIES_LIST = ["AT","BE","BG","CH","CY","CZ","DK","EE","EL","ES","FI","FR","HR","HU","IS",\
                    "IT","LI","LT","LU","LV","MT","NL","NO","PL","PT","RO","SE","SI","SK","DE",\
                    "DE_TOT","AL","IE","ME","MK","RS","AM","AZ","GE","TR","UA","BY","UK","XK",\
                    "FX","MD","SM","RU"]

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

@pytest.fixture(scope="session")
def eurostat_life_expect_raw() -> pd.DataFrame:

    """Fixture to load the raw eurostat file"""
    return pd.read_json(FIXTURES_DIR / "eurostat_life_expect.json")

@pytest.fixture(scope="session")
def eurostat_life_expectancy_expected() -> pd.DataFrame:

    """Fixture to load the raw eurostat file"""
    return pd.read_csv(FIXTURES_DIR / "eurostat_life_expectancy_expected.csv")

@pytest.fixture(scope="session")
def expected_countries_list() -> pd.DataFrame:

    """Fixture to return the list of all countries in enum"""
    return ALL_COUNTRIES_LIST
