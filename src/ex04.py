"""
Execise 4
"""


def area(param1, param2):
    """
    Calculates the area of a rectangle given its length and width.

    Parameters:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.
    """
    # TODO : complete this
    width = param1
    length = param2
    return width * length


def perimeter(param1, param2):
    """
    Calculate the perimeter of a rectangle.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The perimeter of the rectangle.
    """
    # TODO : complete this
    width = param1
    length = param2
    return ( width * 2 ) + ( length * 2 )


def volume(param1, param2, param3):
    """
    Calculates the volume of an object given its length, width, and height.

    Args:
        length (float): The length of the object.
        width (float): The width of the object.
        height (float): The height of the object.

    Returns:
        float: The volume of the object.
    """
    # TODO : complete this
    width = param1
    length = param2
    height = param3
    return width * length * height


def surface_area(param1, param2, param3):
    """
    Calculate the surface area of a rectangular prism.

    Parameters:
        length (float): The length of the rectangular prism.
        width (float): The width of the rectangular prism.
        height (float): The height of the rectangular prism.

    Returns:
        float: The total surface area of the rectangular prism.
    """
    # TODO : complete this
    width = param1
    length = param2
    height = param3
    return (width * length * 2) + (width * height *2) + (length * height *2)
