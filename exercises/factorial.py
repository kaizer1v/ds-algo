def factorial(n=0):
    '''
    Gives factorial of a number

    n! = n * (n - 1)!
    0! = 1

    Parameter
    ---------
    n
        The factorial for which you want
    -------
    int
        the factorial the number
    '''
    if n <= 1:
        return 1
    return n * factorial(n - 1)
