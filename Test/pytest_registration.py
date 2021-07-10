'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-10
@Title : Test cases for user registration system using pytest
/**********************************************************************************
'''
import pytest
import sys
import json
sys.path.insert(0, 'C:/Users/www.abcom.in/Documents/PythonWorkspace/FormRegistration')
from Utility.regex_validation import (validate_name, email_validate, number_validation, password_validate)

pytest.fixture
def read_json():
    """
    Description:
        This method will read json file and return list of name for validating.
    Return:
        It will return list of name for validating
    """
    f = open('samples_for_test.json',)
    data = json.load(f)
    return data

# test case for valid name by reading json file
def test_multiple_names_should_return_true():
    """
    Description:
        Given valid name samples from json file should return false and pass the test. 
    """
    sample_name_list = read_json()
    for name in sample_name_list['valid_name']:
        assert validate_name(name)

# test case for invalid name by reading json file
def test_multiple_names_should_return_false():
    """
    Description:
        Given invalid name samples from json file should return false and pass the test.
    """
    sample_name_list = read_json()
    with pytest.raises(Exception) as exc_info:
        for name in sample_name_list['invalid_name']:
            assert validate_name(name)

# test case for valid last name by reading json file
def test_multiple_last_names_should_return_true():
    """
    Description:
        Given valid last name samples from json file should return false and pass the test. 
    """
    sample_last_name_list = read_json()
    for last_name in sample_last_name_list['valid_last_name']:
        assert validate_name(last_name)

# test case for invalid last_name by reading json file
def test_multiple_last_names_should_return_false():
    """
    Description:
        Given invalid last name samples from json file should return false and pass the test.
    """
    sample_last_name_list = read_json()
    with pytest.raises(Exception) as exc_info:
        for last_name in sample_last_name_list['invalid_last_name']:
            assert validate_name(last_name)

# test case for valid email by reading json file
def test_multiple_emails_should_return_true():
    """
    Description:
        Given valid email samples from json file should return true and pass the test. 
    """
    sample_email_list = read_json()
    for email in sample_email_list['valid_email']:
        assert email_validate(email)

# test case for invalid email by reading json file
def test_multiple_emails_should_return_false():
    """
    Description:
            Given invalid email samples from json file should return false and pass the test. 
    """
    sample_email_list = read_json()
    with pytest.raises(Exception) as exc_info:
        for email in sample_email_list['invalid_email']:
            assert email_validate(email)

# test case for valid password by reading json file
def test_multiple_passwords_should_return_true():
    """
    Description:
        Given valid password samples from json file should return true and pass the test. 
    """
    sample_password_list = read_json()
    for password in sample_password_list['valid_password']:
        assert password_validate(password)

# test case for invalid password by reading json file
def test_multiple_password_should_return_false():
    """
    Description:
            Given invalid password samples from json file should return false and pass the test. 
    """
    sample_password_list = read_json()
    with pytest.raises(Exception) as exc_info:
        for password in sample_password_list['invalid_password']:
            assert password_validate(password)

# test case for valid number by reading json file
def test_multiple_number_should_return_true():
    """
    Description:
        Given valid password samples from json file should return true and pass the test. 
    """
    sample_number_list = read_json()
    for number in sample_number_list['valid_number']:
        assert number_validation(number)

# test case for invalid numbers by reading json file
def test_multiple_numbers_should_return_false():
    """
    Description:
            Given invalid number samples from json file should return false and pass the test. 
    """
    sample_number_list = read_json()
    with pytest.raises(Exception) as exc_info:
        for number in sample_number_list['invalid_number']:
            assert number_validation(number)







