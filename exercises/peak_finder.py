'''
Peak (P) is an element in the list iff

indexof(P) - 1 th element <= P &
indexof(P) + 1 th element <= P

Eg: [5, 9, 3, 4, 2]

Here, 9 is a peak because 5 & 3 both are lte 9
So is 4 a peak, because 3 & 2 are lte 4


Algorithm for 1D Array
----------------------
Run Time: O(log n)

Divide & Conquer way of starting from the mid, point
if left value > mid value, then go left and repeat
if right value > mid value, then go right and repeat


Algorithm for 2D Array
----------------------
Run Time: O(m log n)

The logic would be similar to that of 1D array, but slight change
For a (n x m) 2D array where n = rows & m = columns

Start from a middle column j = m / 2
Look for the global max (which would take O(m) time) within that column
If (i, j - 1) > (i, j) then look to the left on the `i`th row
If (i, j + 1) > (i, j) then look to the right on the `i`th row
'''




# Attempt 1 for 1D array
def find_peak(l):
    '''
    Given a list of elements, find the
    peak value in the list

    Parameters
    ----------
    l : list
        the list of comparable elements you want to find the
        peak in

    Returns
    -------
    list
        a list of peak values and their positions
    '''
    stop = len(l) - 1
    start = 1
    peaks = []
    while start != stop:
        if (l[start - 1] <= l[start]) and (l[start + 1] <= l[start]):
            peaks.append(l[start])
        start += 1
    return peaks



'''
But we've got to do better. Firstly, we need to come up
with "a" peak i.e. a single number (if it even exists)
in the first place. So the problem now becomes from the example
we saw earlier

Eg: [5, 11, 3, 2, 7, 10]

Here, 9 is a peak because 5 <= 9 on the left side &
3, 2 & 7 all are <= 9 on the right side of 9. Thus, 9
becomes the peak of the list

In this case how can we modify our algo to find the peak

Explanation
-----------
Start from a `mid` value.

If l[mid - 1] > l[mid], then look to the left indexes `0` to `mid - 1`
If l[mid + 1] > l[mid], then look to the right indexes `mid` to `(len(l) - 1)`

'''

# Attempt 2 for 1D array
def peak_1d(l):
    '''
    Find "a" peak, if it exists where
    the peak element should be greater than
    both its neighbours.

    NOTE: There can be multiple peaks in a list, but
    this function will return any one of them

    Parameters
    ----------
    l : list
        list of comparable values to find peak in

    Returns
    -------
    int:
        returns the peak
    '''
    def peak(start, stop):
        mid = (start + stop) // 2
        if mid > 0 and l[mid] < l[mid - 1]:
            return peak(start, mid)
        elif mid < len(l) - 1 and l[mid] < l[mid + 1]:
            return peak(mid, stop)
        else:
            return l[mid]
    return peak(0, len(l))


def peak_2d(l):
    '''
    Find a "hill", where the surrounding elements (top, bottom, left & right)
    are smaller than the "hill" value

    Example
    -------
    [[1, 10,  7,  4],
    [[5,  3, 11,  5],
    [[8,  6,  9, 10]]
    Here, 11 is a hill, since it is surrounded by smaller elements


    Parameters
    ----------
    l : 2D list
        the matrix or 2D list within which you want to find the "hill"

    Returns
    -------
    int:
        the value of the "hill"
    '''
    cols = len(l[0])
    start_col = cols // 2
    sel_col = convert_col_to_row(l, start_col)
    sel_row = find_max_ind(sel_col)
    return peak_1d(l[sel_row])


def find_max_ind(l):
    '''
    Given a list of comparable items, find
    the maximum element in the list

    Parameters
    ----------
    l : list
        the list in which you want to find the maximum value

    Returns
    -------
    int
        index of the element with max value
    '''
    i = 0
    maxi = l[i]
    while i != len(l) - 1:
        if l[i] > maxi:
            maxi = l[i]
        i += 1
    return i


def convert_col_to_row(l, i):
    '''
    Given a 2D array, combine all values with a given index of
    a column into a flat array.

    Parameters
    ----------
    l : 2D array
    i : int
        the index of the column to convert into a row

    Returns
    -------
    list
        1D array of combined columns into a row
    '''
    cols_to_row = []
    rows = len(l)
    for r in range(0, rows):
        cols_to_row.append(l[r][i])
    return cols_to_row
