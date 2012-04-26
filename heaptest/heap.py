#!/usr/bin/env python

class Heap:
    "Heap Abstract Data Type"

    def __init__(self, L=None):
        self.data = []
        if L:
            for e in L:
                self.insert(e[0], e[1])

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return ', '.join(["[%s: %s]" % (d[0], d[1]) for d in self.data])

    def findmin(self):
        """Return min element from this heap without removing it. Element
        is an array of size 2 with key at first index and value at second:
        [key, val]"""
        try:
            return self.data[0]
        except:
            raise HeapException, "findmin: Heap empty"

    def extractmin(self):
        """Find and remove min element from this heap. Element is an array
        of size 2 with key at first index and value at second: [key, val]"""
        try:
            if len(self.data) == 1:
                return self.data.pop()
            else:
                m = self.findmin()
                self.data[0] = self.data.pop()
                self._heapify(0)

                return m
        except:
            raise HeapException, "extractmin: Heap empty"

    def insert(self, key, val):
        """Insert key/value pair into this heap. Key/value pair should be
        passed as 2-element array: [key, val]"""
        self.data.append([key, val])
        # Subtract 1 for heapify since we are zero-based
        self._heapify(len(self.data) - 1)

    def changekey(self, index, newkey):
        # Cur key at index 0 of list at self.data[index]
        self.data[index][0] = newkey
        self._heapify(index)

    def _heapify(self, i):
        p = (i - 1) >> 1    # floor((i - 1) / 2)
        l = (i << 1) + 1    # i * 2 + 1
        r = (i << 1) + 2    # i * 2 + 2

        e = self.data[i]

        if i != 0:
            parent = self.data[p]
            if e[0] < parent[0]:
                self._swap(i, p)
                self._heapify(p)

        if len(self.data) > l:          # Check for children
            if len(self.data) - 1 < r:  # Only have left
                left = self.data[l]
                if e[0] > left[0]:
                    self._swap(i, l)
                    self._heapify(l)
            else:                       # Have left and right
                left = self.data[l]
                right = self.data[r]
                if left[0] < right[0]:
                    s = l
                else:
                    s = r
                child = self.data[s]
                if e[0] > child[0]:
                    self._swap(i, s)
                    self._heapify(s)

    def _swap(self, i, j):
        temp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = temp


class HeapException(Exception):
    pass


if __name__ == '__main__':
    P = Heap([[2, 1], [2, 1], [13, 1], [7, 1], [3, 1], [-1, 1]])
    print P

    print "Change Key"
    P.changekey(0, 14)
    print P

    P.insert(77, 1)
    print P

    P.insert(8, 1)
    print P

    P.insert(0, 1)
    print P

    while P:
        print "Extract Min: %s" % (P.extractmin()[0])
        print P
