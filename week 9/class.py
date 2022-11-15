from sys import stdin
from copy import deepcopy


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
        return Matrix([[self.list_new[i][j] + other.list_new[i][j]
                      for j in range(len(self.list_new[0]))]
                      for i in range(len(self.list_new))])

    def __mul__(self, a):
        return Matrix([[el * a for el in row] for row in self.list_new])

    __rmul__ = __mul__


exec(stdin.read())
