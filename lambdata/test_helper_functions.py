"""Unit testing for helper_functions module"""

# imports
import pytest
import helper_functions as hf


# test DataFrame


def test_helper():
    """Testing whether Helper object is a DataFrame"""
    df = pd.DataFrame({
        "A": [1, 2, 3],
        "B": [4, 5, 6],
        "C": [7, 8, 9]
    })
    test_df = Helper(df)
    assert isinstance(test_df, DataFrame)


test_helper()
