"""
Written by Liquid Glass

Useable functions when imported:

1. check_password_conditions(firstPassword, secondPassword)

This function will check if the password matches, followed by the length of the password

If the password goes through all the checks without any issues, the password that is
entered the first attempt will be returned. Otherwise, None will be returned
"""

def check_password_conditions(firstPassword, secondPassword):
        equalPassword = check_equal_password(firstPassword, secondPassword)

        sufficientLength = check_sufficient_length(equalPassword, firstPassword)

        finalPasswordStatus = final_password_check(equalPassword, sufficientLength, firstPassword)

        return finalPasswordStatus

def check_equal_password(firstPassword, secondPassword):
        if firstPassword == secondPassword:
                return int(0)
        else:
                return int(1)

def check_sufficient_length(previousErrorCode, firstPassword):
        if previousErrorCode == int(0):
                if len(firstPassword) >= int(12):
                        return int(0)
                else:
                        return int(1)

        elif previousErrorCode == int(1):
                print("\nYour passwords do not match")


def final_password_check(equalPassword, sufficientLength, firstPassword):
        if sufficientLength == int(1):
                print("\nYour password should be at least 12 characters long")

        if equalPassword or sufficientLength == int(1):
                return None
        else:
                return firstPassword
