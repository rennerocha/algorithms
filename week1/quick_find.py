# -*- coding: utf-8 -*-

class QuickFind(object):

    def __init__(self, array_size):
        self.array = range(0, array_size)
        print "Initilized array: ", self.array
    
    def is_connected(self, p, q):
        return self.array[p] == self.array[q]

    def union(self, p, q):
        if not self.is_connected(p, q):
            value_q = self.array[q]
            value_p = self.array[p]
            for index, value in enumerate(self.array):
                if value == value_p:
                    self.array[index] = value_q
        print "union({0}, {1}) = {2})".format(p, q, self.array)


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
