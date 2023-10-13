"""
Exercise 16
"""


def mode(num_list):
    """
    Calculate the mode of a list of numbers.

    Parameters:
    - num_list (list): A list of numbers.

    Returns:
    - int or None: The mode of the list, or None if the list is empty.
    """
    count = 0
    if num_list.__len__()==0:
        return None
    else:
        for i in num_list:
            new_count = num_list.count(i)
            if new_count > count:
                count = new_count
                mode = i
    return mode