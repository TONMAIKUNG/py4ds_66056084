"""
Exercise 23 : 99 Bottles of Beer on the Wall
"""


def bottles_of_beer(bottle):
    """
    Calculate the number of bottles of beer on the wall.
    And print out like this :

    99 bottles of beer on the wall,
    99 bottles of beer.
    Take one down, pass it around,
    98 bottles of beer on the wall.
    ...
    1 bottle of beer on the wall,
    1 bottle of beer.
    Take one down, pass it around,
    No more bottles of beer on the wall!

    Returns:
        str: The repeated lyrics of bottles of beer on the wall.
    """
    # TODO : complete this
    pass
    if bottle > 1:
        return (f'{bottle}' + ' bottles of beer on the wall,\n' +
                f'{bottle}' + ' bottles of beer.\nTake one down, pass it around,\n' +
                f'{bottle-1}' + ' bottles of beer on the wall.\n')
    else:
        return (f'{bottle}' + ' bottle of beer on the wall,\n' +
                f'{bottle}' + ' bottle of beer.\nTake one down, pass it around,\n' +
                'No more bottles of beer on the wall!\n')

def loop_bottles_of_bears(bottle):
    while bottle > 0:
        print(bottles_of_beer(bottle))
        bottle -= 1


if __name__ == '__main__':
    loop_bottles_of_bears(5)
