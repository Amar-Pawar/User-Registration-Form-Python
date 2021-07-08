'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-08
@Title : User Registration System
/**********************************************************************************
'''
import re
import sys
sys.path.insert(0, 'C:/Users/www.abcom.in/Documents/PythonWorkspace/FormRegistration')
from Utility.regex_validation import (validate_name, email_validate, number_validation, password_validate)
from Utility.logging_handler import logger

class RegistrationForm():
    def __init__(self):
        print("Welcome to user registration")

    def validation(self):
        """
        Description:
            This function will validate user input for different fields.
            It will check from the module imported if input matches the pattern or not. 
        """
        try:
            # UC1-validation for first name
            first_name = input("Enter your name: ")
            first_name_validation_status = validate_name(first_name)

            # UC2-validate last name
            last_name = input("Enter your last name: ")
            last_name_validation_status = validate_name(last_name)

            # UC3-validate email id
            email = input("Enter your email id: ")
            email_validation_status = email_validate(email)

            # UC4-mobile number validation
            mobile_number = input("Enter your contact number: ")
            number_validation_status = number_validation(mobile_number)
            # UC5-6-7-8
            # validate password to have atleast one uppercase letter
            # password to have atleast one numeric
            # password should have exactly one special character
            password = input("Enter your password: ")
            password_validation_status = password_validate(password)

            if (not first_name_validation_status or not last_name_validation_status or not email_validation_status 
            or not number_validation_status or not password_validation_status):
                print("Please enter proper Credentials..")
                self.validation()
                return
            else:
                logger.info("User Registered Successfully")
        except Exception as e:
            logger.info(f"Error!!{e}")

registration_form_object = RegistrationForm()
registration_form_object.validation()
