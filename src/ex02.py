"""
Execise 2
"""


def convert_to_fahrenheit(celsius):
    """
    Convert Celsius temperature to Fahrenheit.

    Args:
        celsius (float): The temperature in Celsius.

    Returns:
        float: The temperature in Fahrenheit.
    """
    # TODO : complete this
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit


def convert_to_celsius(fahrenheit):
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
    - fahrenheit (float): The temperature in Fahrenheit.

    Returns:
    - float: The temperature in Celsius.
    """
    # TODO : complete this
    celsius = (fahrenheit - 32) * (5/9)
    return celsius

def test_convert_two_times(x):
    return round(convert_to_celsius(convert_to_fahrenheit(x)))
