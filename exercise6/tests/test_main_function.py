######################### Imports#################################
from src.__main__ import check_for_positive_and_valid_value, main
import pytest
import argparse
#################################################################

# Test the check_for_positive_and_valid_value function
# Here I tried to create a test that explicitely tests the ArgumentParser implementation yet it shows still that these lines in the __main__.py are not covered.
# I added some more invalid costs and it came to a coverage of 82%


@pytest.mark.parametrize("value, expected", [
    (0, None),  # Test with zero
    (5, None),  # Test with positive integer
    (5.5, None),  # Test with positive float
    (-5, argparse.ArgumentTypeError),  # Test with negative integer
    (-5.5, argparse.ArgumentTypeError),
    (-0.1, argparse.ArgumentTypeError),  # Test with negative float
    ("abc", argparse.ArgumentTypeError),  # Test with non-numeric string
])
def test_check_for_positive_and_valid_value(value: int | float, expected: ValueError | None):
    """
    Check if the values will be checked correctly
    Args:
        value (int | float): valid or invalid value
        expected (ValueError | None): error expected to be raised if the value isn't valid
    """

    if expected:
        with pytest.raises(expected):
            check_for_positive_and_valid_value(value)
    else:
        assert check_for_positive_and_valid_value(value) is None
