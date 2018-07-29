#game theory problems
class Solution(object):
    def canIWin(self, m, total):
        """
        :type m: int
        :type total: int
        :rtype: bool
        """
        #if sum(1..m) < total, nobody can win
        if m*(m+1)/2 <total: return False
        self.memo = {}
        return self._canwin(range(1,m+1), total)
    
    def _canwin(self,pool, total):
        hash = tuple(pool)
        if  hash in self.memo:
            return self.memo[hash]
        
        #base case of the recursion
        #if the max of the available numbers is greater than total, it's a easy win
        if pool[-1] >= total:
            self.memo[hash] = True
            return True
        
        #try all numbers in the pool, find the one that makes opponent can't win.
        for i in range(len(pool)):
            if not self._canwin(pool[:i]+pool[i+1:], total-pool[i]):
                self.memo[hash]=True
                self.memo[tuple(pool[:i]+pool[i+1:])]=False
                return True
                
        #if no such number is found, I can't win
        self.memo[hash] = False
        return False
