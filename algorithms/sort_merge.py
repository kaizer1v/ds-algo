'''
Merge Sort

Given a list of unsorted items, Merge sort uses the technique
of divide and conquer, where it

1. Keeps dividing the list until there's either max of 1 or 2 items in the list
2. Merge these sorted atomic lists until the list is back to the same size as original

It takes O(n log(n)) times only
'''
def sort_merge(l):

    def merge(a, b):
        aux = []
        i, j = 0, 0
        while i < len(a) and j < len(b):
            if a[i] <= b [j]:
                aux.append(a[i])
                i += 1
            else:
                aux.append(b[j])
                j += 1
            if i == len(a):
                aux += b[j:]
            if j == len(b):
                aux += a[i:]
        return aux

    def divide(l):
        size = len(l)
        if size <= 1:
            return l
        mid = size // 2
        left = l[:mid]
        right = l[mid:]

        return merge(divide(left), divide(right))

    return divide(l)
