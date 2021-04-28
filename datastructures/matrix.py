class Matrix:
    '''
    [[1, 2],
     [2, 1]]

    is a matrix
    '''
    def __init__(self, arr):
        self.matrix = arr
        self.height = self.calc_height()
        self.width = self.calc_width()

    def calc_height(self):
        return len(self.matrix)

    def calc_width(self):
        if self._is_valid():
            return len(self.matrix[0])
        else:
            raise Exception('Size of all rows must be same')

    def _is_valid(self):
        '''
        checks if size of each row of the matrix
        is the same
        '''
        f = len(self.matrix[0])
        for a in self.matrix:
            if len(a) != f:
                return False
        return True

    def get_dimension(self):
        return (self.width, self.height)

    def _is_square(self):
        '''
        compute if height & widht of matrix
        is the same
        '''
        return self.width == self.height

    def __repr__(self):
        print( '\n'.join([ ' '.join(list(map(lambda x: str(x), a))) for a in self.matrix ]) )

    def __add__(self, m):
        '''
        adds current matrix with `m`

        | 1 2 |     | 2 1 |     | . . |
        | 2 1 |  +  | 1 2 |  =  | . . |
        '''
        # if not self.get_dimension(m):
        #     return False
        pass

    def __sub__(self, m):
        '''
        substracts current matrix with `m`
        '''
        pass

    def __mul__(self, m):
        '''
        multiplies current matrix with `m`
        '''
        pass

    def eq_size(self, m):
        '''
        checks if current matrix
        and given matrix are of same dimensions
        '''
        return self.get_dimension() == m.get_dimension()

    def __eq__(self, m):
        '''
        checks if current matrix == `m`
        '''
        pass
