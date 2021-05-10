from libs.util import warning


def deprecated(new_function):
    def inner_function(func):
        def wrapper(*args, **kwargs):
            warning("This function is deprecated please use: {}"
                    .format(new_function.__name__))
            func(*args, **kwargs)
        return wrapper

    return inner_function


def singleton(cls: object):
    """Make sure a certain class can only have 1 instance

    Parameters
    ----------
    cls : object
        a new object if it is the first of it's class
        otherwise a already existing instance will be returned
    """
    def wrapper(*args, **kwargs):
        if not wrapper.instance:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper
