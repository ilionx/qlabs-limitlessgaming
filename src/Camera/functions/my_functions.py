"""a set if simple functions"""
from datetime import datetime


def print_on_current_line(*args):
    """
    prints all given *args on the same line

    Parameters
    ----------
    *args
        a set of arguments to print on the current line
    """
    print(*args, end=20 * " " + "\r")


def get_time():
    """
    get the current date and time

    Returns
    -------
    datetime_string:str
        the current time in %H:%M:%S format
    """
    datetime_string = str(datetime.now().time())[:8]
    return datetime_string
