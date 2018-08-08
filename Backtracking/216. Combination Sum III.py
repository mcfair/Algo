#Find all possible combinations of k numbers that add up to a number n, 
#given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        if n < k*(k+1)/2: 
            return []
        
        def dfs(bag, m):
            if len(bag)==k and sum(bag)==n:
                ans.append(bag) 
                return
            
            for i in range(m,10):
                dfs(bag+[i], i+1) #pick from right side to avoid duplicates
                
        ans = []
        dfs([],1)
        return ans
            
            
            
        
