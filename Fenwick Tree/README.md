A Fenwick tree is a wonderful data structure that supports two operations on an array: increment a given value by a given amount, and find the sum of a segment of values, both in O(log n) time.  

```
class BinaryIndexedTree(object):
    #Fenwick Tree index starts from 1 (i.e. 2^0)
    def __init__(self, n):
        self.sums = [0] * (n + 1) 
        
    #O(log n)
    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)
    
    #O(log n), query returns the rangesum from 0 to i
    #to find a segment sum, we use query(right) - query(left-1)
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.sums[i]
            i -= self._lowbit(i)
        return ret
    
    def _lowbit(self, i):
        return i & -i
```
