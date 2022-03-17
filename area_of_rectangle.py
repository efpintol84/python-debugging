#! /usr/bin/env python3

"A script for calculating the area of a rectangle."

import sys


def area_of_rectangle(height, width):
    """
    Returns the area of a rectangle.

    Parameters
    ----------
    height : int or float 
        The height of the rectangle.
    width : int or float
        The width of the rectangle. If `None` width is assumed to be equal to 
        the height.

    Returns
    -------
    int or float
        The area of the rectangle

    Examples
    --------
    >>> area_of_square(7)
    49
    >>> area_of_rectangle (7, 2)
    14
    """
    if width == None:
        width = height
    area = int(height) * int(width)
    area = int(area)
    return area

if __name__ == '__main__':
    for x in sys.argv:
        if (len(sys.argv) < 2) or (len(sys.argv) > 3):
            message = (
                    "{script_name}: Expecting one or two command-line arguments:\n"
                    "\tthe height of a square or the height and width of a "
                    "rectangle".format(script_name = sys.argv[0]))
            sys.exit(message)
        if len(sys.argv) == 1:
             height = sys.argv[1]
             width = height
             continue
        else:
             height = sys.argv[1]
             width = sys.argv[2]

    area = area_of_rectangle(height, width)

    message = "The area of a {h} X {w} rectangle is {a}".format(
            h = height,
            w = width,
            a = area)
    print(message)
