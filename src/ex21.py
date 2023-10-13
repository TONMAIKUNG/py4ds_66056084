"""
Exercise 21 : Validate Date
"""


def is_valid_date(year, month, day):
    """
    Check if a given date is valid.

    Parameters:
        year (int): The year of the date.
        month (int): The month of the date.
        day (int): The day of the date.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    # important to import here
    #from src.sol20 import is_leap_year

    # TODO : complete this
    if (year % 400 == 0 ) or (year % 4 == 0) and (year % 100 != 0):
        if month == 2:
            if day in range(1,30):
                return True
            else:
                return False

        elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            if day in range(1,32) :
                return True
            else:
                return False
        elif (month==4 or month==6 or month==9 or month==11):
            if day in range(1,31) :
                return True
            else:
                return False
        else:
            return False
    else :
        if month == 2:
            if day in range(1,29):
                return True
            else:
                return False

        elif (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
            if day in range(1,32) :
                return True
            else:
                return False
        elif (month==4 or month==6 or month==9 or month==11):
            if day in range(1,31) :
                return True
            else:
                return False
        else:
            return False