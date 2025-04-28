# *args is a special syntax in Python that allows you to pass a variable number of arguments to a function.

def add(*args):
    """
    Add all the arguments together.
    """
    print(args[0])

    # sum = 0
    # for n in args:
    #     sum += n
    # return sum

    return sum(args)
print(add(1, 2, 3, 4, 5))  # Output: 15