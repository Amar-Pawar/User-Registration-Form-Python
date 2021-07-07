'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title : Test cases for user registration system using pytest
/**********************************************************************************
'''
import pytest
import unittest
import sys
sys.path.insert(0, 'C:/Users/www.abcom.in/Documents/PythonWorkspace/FormRegistration')
from Utility.regex_validation import (validate_name)

def test_first_name_should_return_true():
    """
    Description:
        Given valid name should return true and pass the test. 
    """
    assert validate_name("Amar")
    assert validate_name("Isc")

def test_first_name_should_return_flase():
    """
    Description:
        Given invalid name should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert validate_name("amar")
        assert validate_name("!mar")
