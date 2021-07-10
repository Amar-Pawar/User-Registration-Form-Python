'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-09
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
        self.valid_email_list = self.data['valid_email']
        self.invalid_email_list = self.data['invalid_email']
        self.valid_number_list = self.data['valid_number']
        self.invalid_number_list = self.data['invalid_number']
        self.valid_password_list = self.data['valid_password']
        self.invalid_password_list = self.data['invalid_password']
        self.f.close()
    # test case for first name
    def test_first_name_should_return_true(self):
        """
        Description:
            This method will test if input first is valid or not
            Given name should return true and pass the test. 
        """
        self.assertTrue(validate_name("Isa"))
        self.assertTrue(validate_name("Amar"))
    # negative test case for first name
    def test_first_name_should_return_false(self):
        """
        Description:
            Given invalid name should return false and pass the test. 
        """
        self.assertFalse(validate_name("amar"))
        self.assertFalse(validate_name("sa"))
        self.assertFalse(validate_name("123sa"))
        self.assertFalse(validate_name("Ia"))
        self.assertFalse(validate_name("Amar123"))
        self.assertFalse(validate_name("Am@1r"))
        self.assertFalse(validate_name("AMar"))
    # test case for last name
    def test_last_name_should_return_true(self):
        """
        Description:
            Given valid name should return true and pass the test. 
        """
        self.assertTrue(validate_name("Pawar"))
        self.assertTrue(validate_name("Zin"))
    # negative test case for first name
    def test_last_name_should_return_false(self):
        """
        Description:
            Given invalid name should return false and pass the test. 
        """
        self.assertFalse(validate_name("pawar"))
        self.assertFalse(validate_name("ab"))
        self.assertFalse(validate_name("123sa"))
        self.assertFalse(validate_name("Ia"))
        self.assertFalse(validate_name("Pawar123"))
    # test case for email
    def test_email_should_return_true(self):
        """
        Description:
            Given valid email should return true and pass the test. 
        """
        self.assertTrue(email_validate("amar.ar92@ymail.com"))
        self.assertTrue(email_validate("amar.ar92@gmail.in"))
        self.assertTrue(email_validate("amar@co.uk"))
        self.assertTrue(email_validate("pawaramar.pawar@gmail.com"))
        self.assertTrue(email_validate("hr@outlook.in"))    
    # negative test case for email
    def test_email_should_return_false(self):
        """
        Description:
            Given invalid email should return false and pass the test. 
        """
        self.assertFalse(email_validate("1mar.ar92@ymail.com"))
        self.assertFalse(email_validate("amar.ar92@@ymail.com"))
        self.assertFalse(email_validate("am#ar.ar92@ymail.com"))
    # test case for email
    def test_number_should_return_true(self):
        """
        Description:
            Given valid number should return true and pass the test. 
        """
        self.assertTrue(number_validation("91 9028626816"))
        self.assertTrue(number_validation("11 7878787667"))
        self.assertTrue(number_validation("74 7676543907"))
        self.assertTrue(number_validation("19 6776907565"))
    # negative test case for email
    def test_number_should_return_false(self):
        """
        Description:
            Given invalid number should return false and pass the test. 
        """
        self.assertFalse(number_validation("91909090987"))
        self.assertFalse(number_validation("01 7878786567"))
        self.assertFalse(number_validation("91 0909009876"))
    # test case for password
    def test_password_should_return_true(self):
        """
        Description:
            Given valid password should return true and pass the test. 
        """
        self.assertTrue(password_validate("amaArxyx@12"))
        self.assertTrue(password_validate("123@xAyzamar"))
        self.assertTrue(password_validate("Amar@pawar123"))
        self.assertTrue(password_validate("Amar123@pawar"))
    # negative test case for password
    def test_password_should_return_false(self):
        """
        Description:
            Given invalid password should return false and pass the test. 
        """
        self.assertFalse(password_validate("@amarfg"))
        self.assertFalse(password_validate("amar#gsjjd"))
        self.assertFalse(password_validate("87789jhsgg"))
        self.assertFalse(password_validate("Amar@jhsgg"))

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




