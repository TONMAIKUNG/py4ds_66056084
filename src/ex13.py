"""
Exercise 13
"""


def calc_sum(num_list):
    """
    Calculate the sum of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int: The sum of all the numbers in the list.
    """
    if num_list.__len__()==0:
        return 0
    else:
        return sum(num_list)


def calc_prod(num_list):
    """
    Calculates the product of all the numbers in the given list.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        int: The product of all the numbers in the list.
    """
    result = 1
    if num_list.__len__()==0:
        return 1
    else :
        for i in num_list:
            result = result * i
        return result
