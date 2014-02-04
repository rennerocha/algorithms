# -*- coding: utf-8 -*-

class QuickUnion(object):

    def __init__(self, size):
        self.array = range(array_size)

    def is_connected(self, p, q):
        return self._root_of(p) == self._root_of(q)

    def _root_of(self, p):
        while p != self.array[p]:
            p = self.array[p]
        return p

    def union(self, p, q):
        root_p = self._root_of(p)
        root_q = self._root_of(q)
        self.array[root_p] = root_q


if __name__ == '__main__':
    quick_union = QuickUnion(10)
    quick_union.union(4, 3)
    quick_union.union(3, 8)
    quick_union.union(6, 5)
    quick_union.union(9, 4)
    quick_union.union(2, 1)
    quick_union.union(5, 0)
    quick_union.union(7, 2)
    quick_union.union(6, 1)
    quick_union.union(7, 3)
