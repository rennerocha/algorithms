# -*- coding: utf-8 -*-

class QuickUnion(object):

    def __init__(self, array_size):
        self.array = range(0, array_size)
        print "Initilized array: ", self.array
        
    def is_connected(self, p, q):
        return self._root_of(p) == self._root_of(q)

    def _root_of(self, q):
        while q != self.array[q]:
            q = self.array[q]
        return q

    def union(self, p, q):
        self.array[self._root_of(p)] = self._root_of(q)
        print "union({0}, {1}) = {2})".format(p, q, self.array)


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
