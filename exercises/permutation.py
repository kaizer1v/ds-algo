import factorial

def permutation(n, r):
    '''
    Gives number of permutations possible

    Example: How many permutations can you get if
        you have `n` objects and want to get `r`
        items in each permutation?

              n!
    nPr = ----------
           (n - r)!

    Parameters
    ----------
    n
        The total items you have
    r
        The count of permutations you want

    Returns
    -------
    int
        total permutations possible
    '''
    return factorial(n) // factorial(n - r)
