import myfun.is_leap
import pytest

def test_leap():
  assert is_leap(1992)==True

def test_centruries_leap():
  assert is_leap(2000)==True

def test_centruries_nonleap():
  assert is_leap(1900)==False

def test_nonleap():
  assert is_leap(1995)==False
  

