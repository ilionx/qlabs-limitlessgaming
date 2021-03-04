def deprecated(new_function):
    def inner_function(func):
        def wrapper(*args, **kwargs):
            print(
                f"WARNING: this function is deprecated please use: \
{new_function.__name__} as replacement")
            func(*args, **kwargs)
        return wrapper

    return inner_function
