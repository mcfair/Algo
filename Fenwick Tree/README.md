A Fenwick tree is a data structure that supports two operations on an array: increment (add) a given value by a given amount, and find (query) the sum of a segment of values, both in O(log n) time.  

https://www.youtube.com/watch?v=2SVLYsq5W8M&t=1037s
 
https://www.youtube.com/watch?v=WbafSgetDDk&t=908s

https://leetcode.com/problems/reverse-pairs/discuss/97268/General-principles-behind-problems-similar-to-%22Reverse-Pairs%22

```
class BinaryIndexedTree(object):
    #Fenwick Tree index starts from 1 (i.e. 2^0)
    def __init__(self, n):
        self.sums = [0] * (n + 1) 
        
    #O(log n)
    def add(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)
    
    #O(log n), query returns the rangesum from 0 to i, it's actually "i-1" in original array
    #to find a segment sum, we use query(right+1) - query(left), "+1" because Fenwick tree index starts from 1
    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.sums[i]
            i -= self._lowbit(i)
        return ret
    
    def _lowbit(self, i):
        return i & -i
```
