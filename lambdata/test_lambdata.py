"""Basic Unit Tests for Lambdata package"""

from random import randint
import pytest
import lambdata_esgalan as lde


def test_increment_int():
    """Making sure increment works for integers"""
    x0 = 0
    y0 = lde.increment(x0)  # 1
    assert y0 == 1

    x1 = 100
    y1 = lde.increment(x1)  # 101
    assert y1 == 101


def test_increment_float():
    """Making sure increment works for floats"""
    x0 = 10.5
    y0 = lde.increment(x0)  # 11.5
    assert y0 == 11.5


def test_increment_neg_int():
    """Making sure increment works for neg integers"""
    x0 = -1
    y0 = lde.increment(x0)  # 0
    assert y0 == 0


def test_increment_neg_float():
    """Making sure increment works for neg floats"""
    x0 = -1.5
    y0 = lde.increment(x0)  # - 0.5
    assert y0 == -0.5


def test_colors():
    """Testing that colors contains correct items"""
    assert "Cyan" in lde.COLORS
    assert "Mauve" in lde.COLORS
    assert "Blue" in lde.COLORS
    assert "Brown" in lde.COLORS
    assert "Yellow" in lde.COLORS
