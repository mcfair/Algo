class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """ 
        def isvalid(t):
            return t==t[::-1]
        
        def backtrack(k, combo):
            if k==len(s):
                ans.append(combo)
                return
            for i in range(k+1,len(s)+1):
                if isvalid(s[k:i]):
                    backtrack(i, combo+[s[k:i]])
            
        ans=[]
        backtrack(0, [])
        return ans
