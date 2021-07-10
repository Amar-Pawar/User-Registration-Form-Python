'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-09
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


# test case for first name
def test_first_name_should_return_true():
    """
    Description:
        Given valid name should return true and pass the test. 
    """
    assert validate_name("Amar")
    assert validate_name("Isc")
# negative test case for first name
def test_first_name_should_return_false():
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
# test case for email
def test_email_should_return_true():
    """
    Description:
        Given valid email should return true and pass the test. 
    """
    assert email_validate("amar.ar92@ymail.com")
    assert email_validate("amar.ar92@gmail.in")
    assert email_validate("amar@co.uk")
    assert email_validate("pawaramar.pawar@gmail.com")
    assert email_validate("amar@co.uk")
    assert email_validate("hr@outlook.in")
# negative test case for email
def test_email_should_return_false():
    """
    Description:
        Given invalid email should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert email_validate("@mar.ar92@@ymail.com")
        assert email_validate("1mar.ar92@ymail.com")
        assert email_validate("amar.ar92@@ymail.com")
        assert email_validate("am#ar.ar92@ymail.com")
# test case for mobile number
def test_number_should_return_true():
    """
    Description:
        Given valid mobile number should return true and pass the test. 
    """
    assert number_validation("91 9028626816")
    assert number_validation("83 8787878780")
    assert number_validation("72 8989894543")
    assert number_validation("24 1234345656")
# negative test case for mobile number
def test_number_should_return_false():
    """
    Description:
        Given invalid mobile should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert number_validation("909899098909")
        assert number_validation("91 0909876789")
        assert number_validation("01 9090987678")
# test case for password
def test_password_should_return_true():
    """
    Description:
        Given valid password should return true and pass the test. 
    """
    assert password_validate("amaArxyx@12")
    assert password_validate("123x@yAzamar")
    assert password_validate("Amar@pawar123")
    assert password_validate("amaArxyx@1")
# negative test case for password
def test_password_should_return_false():
    """
    Description:
        Given invalid password should return false and pass the test. 
    """
    with pytest.raises(Exception) as exc_info:
        assert password_validate("@amar")
        assert password_validate("12@adas345h")
        assert password_validate("@assdfdgb#")
        assert password_validate("@assdf1dgb#")
        assert password_validate("@aAssdfdgb")

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







