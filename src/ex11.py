"""
Exercise 11
"""


def get_hr_min_sec(tsec):
    """
    Generates a string representation of the given number
    of seconds in the format "9h 9m 9s".

    Args:
        tsec (int): The number of seconds to convert to
        the "9h 9m 9s" format. Default is 0s.

    Returns:
        str: A string representation of the given
        number of seconds in the "9h 9m 9s" format.

    Example:
        >>> get_hr_min_sec(3665)
        '1h 1m 5s'
        >>> get_hr_min_sec(0)
        '0s'
    """
    hour = tsec // 3600
    x = tsec % 3600
    minutes = x // 60
    seconds = x % 60

    if hour == 0 and minutes != 0 and seconds != 0:
        return "%sm %ss" %(minutes, seconds)
    elif hour != 0 and minutes == 0 and seconds != 0:
        return "%sh %ss" %(hour, seconds)
    elif hour != 0 and minutes != 0 and seconds == 0:
        return "%sh %sm" %(hour, minutes)
    elif hour != 0 and minutes == 0 and seconds == 0:
        return "%sh" %(hour)
    elif hour == 0 and minutes != 0 and seconds == 0:
        return "%sm" %(minutes)
    elif hour == 0 and minutes == 0 and seconds != 0:
        return "%ss" %(seconds)
    elif hour == 0 and minutes == 0 and seconds == 0:
        return "%ss" %(seconds)
    else:
        return "%sh %sm %ss" %(hour , minutes , seconds)