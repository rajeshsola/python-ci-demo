from myfun import *
import pytest

def test_even():
    assert is_even(44)==True

def test_odd():
    assert is_even(45)==False
    
def test_equilateral():
    assert type_of_triangle(10,10,10)==1
    
def test_isosceles():
    assert type_of_triangle(10,10,8)==2
    
def test_scalan():    
    assert type_of_triangle(3,4,5)==3
    
def test_leap():
    assert is_leap(1992)==True

def test_nonleap():
    assert is_leap(1995)==False
# https://coverage.readthedocs.io/en/7.6.1/
    
# https://coverage.readthedocs.io/en/7.6.1/
