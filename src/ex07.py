"""
Execise 7
"""


def print_ASCII_table(start_char,end_char):
    """
    Generate and print the ASCII table for a range of characters.

    Args:
        start_char (int): The ASCII value of the starting character.
        end_char (int): The ASCII value of the ending character.

    Returns:
        str: Returns nothing. The function simply prints the ASCII characters.

    """
    # TODO : complete this
    while start_char <= end_char:
        x = chr(start_char)
        print(x)
        start_char += 1
