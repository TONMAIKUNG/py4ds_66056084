"""
Exercise 15
"""


def median(numlist):
    """
    Calculate the median of a list of numbers.

    Parameters:
        num_list (list): A list of numbers.

    Returns:
        [int, None]: The median value of the list, or None if the list is empty.
    """
    if numlist.__len__() == 0:
     return None
    numlist.sort()
    middle_num=len(numlist) // 2
    if len(numlist) % 2 == 0:
        return (numlist[middle_num]+numlist[middle_num-1])/2
    else :
        return numlist[middle_num]




