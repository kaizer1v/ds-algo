'''
Selection Sort

1. Iterate through the list of items to find the `smallest` one first
2. Swap that with the item at the 1st element in the list
'''

def sort_selection(items, asc=True):
    '''
    Selection Sort

    Uses 2 steps to sort in order
    1. Find the minimum
    2. Swap with i (i starts from 0 & increments by 1)

    Run Time: O(n^2)

    Parameters
    ----------
    items : list
        the list of items to be sorted

    Returns
    -------
    list
        in a sorted order
    '''
    l = items
    i = 0
    fn = find_min
    if asc == False:
        fn = find_max

    for i in range(len(l)):
        # 1. get min from the list
        min_i = fn(l[i:])

        # 2. swap
        l[i], l[i + min_i] = l[i + min_i], l[i]

    return l


def find_min(l):
    # Find index of minimum from a list
    length = len(l)
    mi = 0
    m = l[mi]

    for ind in range(mi + 1, length):
        if l[ind] < m:
            m = l[ind]
            mi = ind

    return mi


def find_max(l):
    # Find index of maximum value from list
    length = len(l)
    mi = 0
    m = l[mi]

    for ind in range(mi + 1, length):
        if l[ind] > m:
            m = l[ind]
            mi = ind

    return mi


def find_min_max(l):
    # Find index of minmum, maximum from a list
    length = len(l)
    i_mini, i_maxi = 0, 0
    mini = l[i_mini]
    maxi = l[i_mini]

    for ind in range(i_mini + 1, length):
        if l[ind] < mini:
            mini = l[ind]
            i_mini = ind
        elif l[ind] > maxi:
              maxi = l[ind]
              i_maxi = ind

    return i_mini, i_maxi
