from sys import stdin
from copy import deepcopy


class MatrixError(BaseException):
    def __init__(self, Matrix, other):
        self.matrix1 = Matrix
        self.matrix2 = other


class Matrix:
    def __init__(self, list_old):
        self.list_new = deepcopy(list_old)

    def __str__(self):
        all_str = ''
        for elem in self.list_new:
            all_str += '\t'.join(map(str, elem)) + '\n'
        return all_str[:-1]

    def size(self):
        return len(self.list_new), len(self.list_new[0])

    def __add__(self, other):
        if len(self.list_new) == len(other.list_new):
            res = [[self.list_new[i][j] + other.list_new[i][j]
                    for j in range(len(self.list_new[0]))]
                   for i in range(len(self.list_new))]
        else:
            raise MatrixError(self, other)
        return Matrix(res)

    def __mul__(self, a):
        return Matrix([[el * a for el in row] for row in self.list_new])

    @staticmethod
    def transposed(self):
        resulf_of_tr = list(zip(*self.list_new))
        return Matrix(resulf_of_tr)

    def transpose(self):
        self.list_new = [[num[i] for num in self.list_new]
                         for i in range(len(self.list_new[0]))]
        return Matrix(self.list_new)

    __rmul__ = __mul__

exec(stdin.read())
