'''
Palindrome Checker

`Madam` is a palindrome, so is `Nitin`.

DATA STRUCTURE USED
Double-Ended Queue

HOW?
The best way to check whether a word is to put it
in a double ended queue
'''
from queue import DoubleEndedQueue


def palindrome_checker(st):
    '''
    Given a string, checks if it is a palindrome

    Parameters
    ----------
    st : string
        to string to be checked

    Returns
    -------
    bool
        True if is a palindrome
        False if not a palindrome

    Raises
    ------
    TypeError
        when `st` is not a string
    '''
    dq = DoubleEndedQueue()
    for s in st:
        dq.add(s)

    while len(dq) >= 1:
        if dq.lpop() != dq.rpop():  # pop will reduce len by 2 everytime, both from r & l
            return False
    return True
