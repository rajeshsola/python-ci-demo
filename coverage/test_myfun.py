from myfun import *
import pytest

def test_even():
    assert is_even(44)==True

def test_odd():
    assert is_even(45)==False
    
# https://coverage.readthedocs.io/en/7.6.1/
