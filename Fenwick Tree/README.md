```
class BinaryIndexedTree(object):
    def __init__(self, n):
        self.sums = [0] * (n + 1) #Fenwick Tree index starts from 1 (i.e. 2^0)

    def update(self, i, delta):
        while i < len(self.sums):
            self.sums[i] += delta
            i += self._lowbit(i)

    def query(self, i):
        ret = 0
        while i > 0:
            ret += self.sums[i]
            i -= self._lowbit(i)
        return ret
    
    def _lowbit(self, i):
        return i & -i
```
