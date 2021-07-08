'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-07
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-08
@Title : User Registration System Validation by Regular Expressions
/**********************************************************************************
'''
from Utility.logging_handler import logger
import re

def validate_name(name):
    """
    Description:
        This function will will check the input by user for first name and last name and complie and match by using
        regular expression and see if pattern matches for validation. 
    Parameters:
        This function takes user input value as parameter to compile with regular expresion
    Return:
        It will return boolean value stored in variable
    """
    try:
        # regex for username for first name and last name
        pattern = re.compile("^[A-Z]{1}[a-z]{2,}$")
        validation_status = re.match(pattern,name)
        if not validation_status:
            print("Name should contain only letters and min 3 characters and first letter should be capital Example: Amar")
    except Exception as e:
        logger.info(f"Errorr!! {e}")
    return validation_status

def email_validate(email):
    """
    Description:
        This function will check the input by user for email id and complie and match by using
        regular expression and see if pattern matches for validation. 
    Parameters:
        This function takes user input value for email as parameter to compile with regular expresion
    Return:
        It will return boolean value stored in variable
    """
    try:
        # regex for email
        pattern = re.compile("^[A-Z a-z]{1,}([+-_.]*)[A-Z a-z 0-9 _+-.]*[@]{1}[A-Z a-z 0-9 +_-]{1,}[.]{1}[a-z]{2,3}([.]{1}[a-z]{2})*$")
        validation_status = re.match(pattern,email)
        if not validation_status:
            print("Enter proper email address")
    except Exception as e:
        logger.info(f"Errorr!! {e}")
    return validation_status

def number_validation(number):
    """
    Description:
        This function will check the input by user for mobile number and complie and match by using
        regular expression and see if pattern matches for validation. 
    Parameters:
        This function takes user input value for mobile number as parameter to compile with regular expresion
    Return:
        It will return boolean value stored in variable
    """
    try:
        # regex for contact number
        pattern = re.compile("^[1-9]{2}\\s{0,1}[1-9]{1}[0-9]{9}$")
        validation_status = re.match(pattern,number)
        if not validation_status:
            print("Enter correct mobile number!! Example 91 9028626816")
    except Exception as e:
        logger.info(f"Errorr!! {e}")
    return validation_status

def password_validate(password):
    """
    Description:
        This function will check the input by user for password and complie and match by using
        regular expression and see if pattern matches for validation. 
    Parameters:
        This function takes user input value for password as parameter to compile with regular expresion
    Return:
        It will return boolean value stored in variable
    """
    try:
        # regex for password
        pattern = re.compile("(?=.*[A-Z])(?=.*[0-9])(?=.*[@_$%&])([A-Z0-9a-z]).{8,20}$")
        validation_status = re.match(pattern,password)
        if not validation_status:
            print("Enter proper password")
    except Exception as e:
        logger.info(f"Errorr!! {e}")
    return validation_status

