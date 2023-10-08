"""
Execise 6
"""


def ordinal_suffix(param):
    """
    Return the ordinal suffix for a given number.

    Parameters:
        num (int): The number for which to find the ordinal suffix.

    Returns:
        str: The ordinal suffix corresponding to the given number.
    """
    # TODO : complete this
    number = param % 100
    if number == 1:
        return '%dst'%param
    elif number == 2:
        return '%dnd'%param
    elif number == 3:
        return '%drd'%param
    else :
        return '%dth'%param
