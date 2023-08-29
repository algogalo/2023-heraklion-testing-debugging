from math import isclose
import numpy as np
from numpy.testing import assert_allclose

def test_sum_int():
    assert 1+2 == 3

def test_sum_float():
    assert isclose(1.1+2.2, 3.3)

def test_sum_array():
    x = np.array([1, 1])
    y = np.array([2, 2])

    expected = np.array([3, 3])
    assert_allclose(x+y, expected)
