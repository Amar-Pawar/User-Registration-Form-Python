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

# test case for first name
def test_first_name_should_return_true():
    """
    Description:
        Given valid name should return true and pass the test. 
    """
    assert validate_name("Amar")
    assert validate_name("Isc")
# negative test case for first name
def test_first_name_should_return_flase():
    """
    Description:
        Given invalid name should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert validate_name("amar")
        assert validate_name("!mar")
        assert validate_name("1amar")
        assert validate_name("AMmar")
        assert validate_name("Amar@")
        assert validate_name("Amar1")
# test case for last name
def test_last_name_should_return_true():
    """
    Description:
        Given valid last name should return true and pass the test. 
    """
    assert validate_name("Pawar")
    assert validate_name("Isc")
# negative test case for last name
def test_last_name_should_return_flase():
    """
    Description:
        Given invalid last name should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert validate_name("pawar")
        assert validate_name("p!mar")
        assert validate_name("1mhatre")
        assert validate_name("PAtil")
        assert validate_name("Mhatre@")
        assert validate_name("paWar")

