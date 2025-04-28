def add(*args):
    """
    Add all the arguments together.
    """
    for n in args:
        print(n, type(n))
add(1, 2, 3, 4, 5)