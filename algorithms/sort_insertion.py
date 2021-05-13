'''
Insertion Sort

Given a list of items and the comparison logic, it will
sort the list in O(n^2) time.


Time
----
O(n^2)

Logic / Algorithm
-----------------
-> Start from the 2nd element in the list (index)
-> Compare with the previous element (prev)
    => If `index` < `prev`, then swap it
-> Move index by +1

Essentially, find the position of 1 element at a time

'''

def compare_fn(a, b, key):
    '''
    A comparison function that can compare two
    integers, strings or dictionaries

    Parameters
    ----------
    a : int, str or dictionary
        the value to compare with `b`
    b : int, str or dictionary
        should be same type as `a`
    key : str
        if the `a` and `b` are of type `dict`
        then the key for the dict to be compared

    Returns
    -------
    int
        -1: if a < b
         0: if a == b
         1: if a > b
    '''
    if key == None:
        a, b = a, b
    else:
        a, b = a[key], b[key]

    if a < b:
        return -1
    elif a > b:
        return 1
    return 0


def sort_insertion(items, fn=compare_fn, key=None):
    '''
    Sorting algorithm using insertion sort

    Run Time: O(n^2)

    Parameters
    ----------
    items : list
        the list of items to be sorted
    fn : callback function (optional)
        a custom function for comparison
        to compare values
    key : str (optional)
        provide `key` of the dict only
        if `items` contains `dict` values.
        Defaults to None

    Returns
    -------
    list
        a sorted list of items in
        ascending order
    '''
    l = len(items)
    for i in range(0, l):
        for j in range(i + 1, l):
            if fn(items[i], items[j], key) > 0:
                items[i], items[j] = items[j], items[i]
    return items
