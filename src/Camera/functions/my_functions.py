"""a set if simple functions"""
from datetime import datetime

def print_on_current_line(*args):
    """prints all given *args on the same line"""
    print(*args, end=20 * " " + "\r")

def get_time():
    """returns the current date and time"""
    return str(datetime.now().time())[:8]
