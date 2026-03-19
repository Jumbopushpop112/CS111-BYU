# Remember to import from the lab06 file and pytest
from lab06 import *
import pytest
# Write your test code here for Q1

def test_product():
    assert product(5) == 120
    assert product(4) == 24
    with pytest.raises(ValueError):
        product(0)
    with pytest.raises(ValueError):
        product(-4)
def test_summation():
    assert summation(4) == 10
    assert summation(5) == 15
    with pytest.raises(ValueError):
        summation("Hey")
    with pytest.raises(ValueError):
        summation(1.234)


# Q2
#####################################

def test_square():
    """*** YOUR CODE HERE ***"""
    assert square(4) == 16
    assert square(5) == 25

def test_sqrt():
    """*** YOUR CODE HERE ***"""
    assert sqrt(4) == 2
    assert sqrt(9) == 3
def test_mean():
    """*** YOUR CODE HERE ***"""
    assert mean([1,2,3]) == 2
    assert mean([1,1,3,4,1]) == 2
    with pytest.raises(AssertionError):
        mean(1)
    with pytest.raises(AssertionError):
        mean([])

def test_median():
    """*** YOUR CODE HERE ***"""
    assert median([1,4,5,6,7]) == 5
    assert median([1,6,7,8,9]) == 7
    with pytest.raises(AssertionError):
        median(5)
    with pytest.raises(AssertionError):
        median([])


def test_mode():
    """*** YOUR CODE HERE ***"""
    assert mode([1,1,2,2]) == 1
    assert mode([1,2,3,4,1,5]) == 1
    with pytest.raises(AssertionError):
        mode("Hi")
    with pytest.raises(AssertionError):
        mode([])

def test_std_dev():
    """*** YOUR CODE HERE ***"""
    assert(std_dev([1,2,3,4])) == pytest.approx(std_dev([1,2,3,4]))
    assert(std_dev([1,2,3,4,5,6])) == pytest.approx(std_dev([1,2,3,4,5,6]))
    with pytest.raises(AssertionError):
        std_dev("Hey")
    with pytest.raises(AssertionError):
        std_dev([])

def test_stat_analysis():
    """*** YOUR CODE HERE ***"""
    assert(stat_analysis([1,1,1,2,3])) == {"mean":1.6, "median":1, "mode":1,"std_dev":pytest.approx(std_dev([1,1,1,2,3]))}
    assert(stat_analysis([5,5,6,7,8])) == {"mean":6.2, "median":6, "mode":5, "std_dev":pytest.approx(std_dev([5,5,6,7,8]))}
    with pytest.raises(AssertionError):
        stat_analysis(5)
    with pytest.raises(AssertionError):
        stat_analysis([])
# OPTIONAL
#####################################

def test_accumulate():
    """*** YOUR CODE HERE ***"""


def test_product_short():
    """*** YOUR CODE HERE ***"""


def test_summation_short():
    """*** YOUR CODE HERE ***"""


def test_invert():
    """*** YOUR CODE HERE ***"""


def test_change():
    """*** YOUR CODE HERE ***"""


def test_invert_short():
    """*** YOUR CODE HERE ***"""


def test_change_short():
    """*** YOUR CODE HERE ***"""
