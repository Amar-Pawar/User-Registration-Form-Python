'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-10
@Title : Test cases for user registration system using unittest
/**********************************************************************************
'''
import sys
sys.path.insert(0, 'C:/Users/www.abcom.in/Documents/PythonWorkspace/FormRegistration')
import json
import unittest
from Utility.logging_handler import logger
from Utility.regex_validation import (number_validation, validate_name, email_validate, password_validate)

class TestCalc(unittest.TestCase):
    def setUp(self):
        self.f = open('samples_for_test.json', 'r')
        self.data = json.load(self.f)
        self.valid_name_list = self.data['valid_name']
        self.invalid_name_list = self.data['invalid_name']
        self.valid_last_name_list = self.data['valid_last_name']
        self.invalid_last_name_list = self.data['invalid_last_name']
        self.valid_email_list = self.data['valid_email']
        self.invalid_email_list = self.data['invalid_email']
        self.valid_number_list = self.data['valid_number']
        self.invalid_number_list = self.data['invalid_number']
        self.valid_password_list = self.data['valid_password']
        self.invalid_password_list = self.data['invalid_password']
        self.f.close()

    # test case for valid first name by reading json file
    def test_first_name_by_reading_json_should_return_true(self):
        """
        Description:
            Given valid name samples from json file should return false and pass the test. 
        """
        for name in self.valid_name_list:
            self.assertTrue(validate_name(name))

    # test case for invalid name by reading json file
    def test_first_name_by_reading_json_should_return_false(self):
        """
        Description:
            Given invalid name samples from json file should return false and pass the test.
        """
        for name in self.invalid_name_list:
            self.assertFalse(validate_name(name))

    # test case for valid last name by reading json file
    def test_last_name_by_reading_json_should_return_true(self):
        """
        Description:
            Given valid last name samples from json file should return false and pass the test. 
        """
        for last_name in self.valid_last_name_list:
            self.assertTrue(validate_name(last_name))

    # test case for invalid last name by reading json file
    def test_last_name_by_reading_json_should_return_false(self):
        """
        Description:
            Given invalid last name samples from json file should return false and pass the test.
        """
        for last_name in self.invalid_last_name_list:
            self.assertFalse(validate_name(last_name))


    # test case for valid email by reading json file
    def test_email_by_reading_json_should_return_true(self):
        """
        Description:
            Given valid email samples from json file should return true and pass the test. 
        """
        for email in self.valid_email_list:
            self.assertTrue(email_validate(email))
    # test case for invalid email by reading json file
    def test_email_by_reading_json_should_return_false(self):
        """
        Description:
             Given invalid email samples from json file should return false and pass the test. 
        """
        for email in self.invalid_email_list:
            self.assertFalse(email_validate(email))

    # test case for valid numbers by reading json file
    def test_numbers_by_reading_json_should_return_true(self):
        """
        Description:
            Given valid number samples from json file should return true and pass the test. 
        """
        for number in self.valid_number_list:
            self.assertTrue(number_validation(number))
    # test case for invalid numbers by reading json file
    def test_numbers_by_reading_json_should_return_false(self):
        """
        Description:
             Given invalid number samples from json file should return false and pass the test. 
        """
        for number in self.invalid_number_list:
            self.assertFalse(number_validation(number))

    # test case for valid passwords by reading json file
    def test_passwords_by_reading_json_should_return_true(self):
        """
        Description:
            Given valid password samples from json file should return true and pass the test. 
        """
        for password in self.valid_password_list:
            self.assertTrue(password_validate(password))
    # test case for invalid password by reading json file
    def test_passwords_by_reading_json_should_return_false(self):
        """
        Description:
             Given invalid password samples from json file should return false and pass the test. 
        """
        for password in self.invalid_password_list:
            self.assertFalse(password_validate(password))




