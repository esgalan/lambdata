"""Unit testing for lambdata package"""

# imports
import pytest
from lambdata.helper_functions import Helper
import pandas as pd


#  test df
df = pd.DataFrame({
    "A": [1, 2, 3],
    "B": [4, 5, 6],
    "C": [7, 8, 9]
})


def test_helper():
    """Testing whether Helper object is a DataFrame"""
    test_df = Helper(df)
    assert isinstance(test_df, Helper)


def test_null_count():
    """Testing null_count function"""
    test_df = Helper(df)
    assert test_df.null_count() == 0
