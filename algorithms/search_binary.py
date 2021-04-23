'''
Binary Search

is a divide and conquer type of algorithm
'''

def binary_search(l, elem):
  '''
  Given a list of items, the function
  searches for whether the `elem` exists
  in the list or not

  Run Time: O(log(n))

  Parameters
  ----------
  l : list
      the list of items to be searched within
  elem :
      the value to be searched for

  Returns
  -------
  boolean
      True:   if `elem` exists in `l`
      False:  if `elem` does not exist in `l`
  '''
  if len(l) == 1 and l[0] != elem:
    return False

  mid = len(l) // 2
  if l[mid] == elem:
    return True

  if elem > l[mid]:
    # look on right-hand-side
    new_l = l[mid + 1:]
  else:
    # look on left-hand-side
    new_l = l[:mid]

  return binary_search(new_l, elem)


def binary_search_loop(l, elem):
  if len(l) == 1 and l[0] != elem:
    return False

  low = 0
  high = len(l) - 1

  while low <= high:
    mid = (low + high) // 2

    if l[mid] == elem:
      return True
    elif elem < l[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return False


'''
works if the list is in reverse order
'''
def binary_search_v2(l, elem, asc):
  if len(l) == 1 and l[0] != elem:
    return False

  mid = len(l) // 2
  if l[mid] == elem:
    return True

  if elem > l[mid]:
    new_l = l[mid + 1:] if asc == True else l[:mid]
  else:
    new_l = l[:mid] if asc == True else l[mid + 1:]

  return binary_search(new_l, elem, asc)


'''
In case of duplicates within a sorted (ascending) list,
return the item with the smallest index, for example
list    ->     [1, 2, 3, 3, 4]
indexes ->      0  1  2  3  4
incase of searching for element 3, return the index 2
'''

# cannot be recursive
def binary_search_with_duplicates(l, elem):
  if len(l) == 1 and l[0] != elem:
    return False

  low = 0
  high = len(l) - 1

  while low <= high:
    mid = (low + high) // 2

    if l[mid] == elem:
      if l[mid - 1] != elem:
        return mid
      else:
        i = mid
        while l[mid] == elem:
          i -= 1
        return i
    elif elem < l[mid]:
      high = mid - 1
    else:
      low = mid + 1

  return False
