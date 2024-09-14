"""A simple module."""


def is_leap(yy):
    """Functin to check given year is leap or not."""
    return yy % 400 == 0 or (yy % 4 == 0 and yy % 100 != 0)

    
