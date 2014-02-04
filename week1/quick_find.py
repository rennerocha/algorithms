# -*- coding: utf-8 -*-

class QuickFind(object):

    def __init__(self, size):
        self.array = range(array_size)

    def is_connected(self, p, q):
        return self.array[p] == self.array[q]

    def union(self, p, q):
        if not self.is_connected(p, q):
            idp = self.array[p]
            idq = self.array[q]
            self.array = [ idq if v == idp else v for v in self.array ]


if __name__ == '__main__':
    quick_find = QuickFind(10)
    quick_find.union(4, 3)
    quick_find.union(3, 8)
    quick_find.union(6, 5)
    quick_find.union(9, 4)
    quick_find.union(2, 1)
    quick_find.union(8, 9)
    quick_find.union(5, 0)
    quick_find.union(7, 2)
    quick_find.union(6, 1)
