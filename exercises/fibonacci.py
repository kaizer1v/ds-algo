def fibonacci_seq(n=5):
    '''
    Gives fib sequence until the `n`

    This algo takes only the last 2 items from the list
    and takes the sum of them and appends it to the same list

    Parameters
    ----------
    n: int
        The `n` until which you want the fib sequence

    Returns
    -------
    list
        the list of fib sequence
    '''
    if n <= 0:
        return n
    f = [0, 1]
    for i in range(2, n):
        f.append(f[i - 1] + f[i - 2])
    return f



def get_nth_fibonacci(n):
    '''
    Get the nth fibonacci number in sequence

    Parameters
    ----------
    n: int
        the `n`th number in the sequence you want

    Returns
    -------
    int:
        The nth number in sequence
    '''
    return fibonacci_seq(n)[n - 1]


def sum_fibonacci(n=5):
    '''
    Gives sum of `n` fibonacci numbers

    Parameters
    ----------
    n: int
        The `n` until which you want sum of

    Returns
    -------
    int
        the sum of fib sequence
    '''
    pass
