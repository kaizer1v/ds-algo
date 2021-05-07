'''
Binary Heap

               (16)             -> index = 1
               /  \
             14  10             -> index = 2, 3
            / \  / \
           8  7 9   3           -> index = 4, 5, 6 & 7


'''

class BinaryHeap:

    def __init__(self):
        self.h = [None]

    def parent(self, ind):
        return ind // 2

    def left(self, ind):
        return 2 * ind

    def right(self, ind):
        return (2 * ind) + 1

    def root(self):
        return self.h[1]

    def add(self, e):
        self.h.append(e)

    def moveup(self):
        pass

    def movedown(self):
        pass
