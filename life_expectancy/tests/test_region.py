from typing import List
import numpy as np
from life_expectancy.region import Region


def test_all_regions(expected_countries_list: List[str]):

    """
    Test for the obtaining of a countries list.
    """
    actual_region_list = Region.get_all_countries()
    np.testing.assert_array_equal(actual_region_list, expected_countries_list)
