'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-07
@Title : User Registration System
/**********************************************************************************
'''
import re
import sys
sys.path.insert(0, 'C:/Users/www.abcom.in/Documents/PythonWorkspace/FormRegistration')
from Utility.regex_validation import (validate_name)
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
        # UC1-validation for first name
        first_name = input("Enter your name: ")
        first_name_validation_status = validate_name(first_name)

        if not first_name_validation_status:
            self.validation()
            return
        else:
            logger.info("User Registered Successfully")

registration_form_object = RegistrationForm()
registration_form_object.validation()
