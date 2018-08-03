class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits: return []
        codec = {2:'abc', 3:'def', 4:'ghi',5:'jkl', 6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        
        letters = [codec[int(i)] for i in digits]
        
        return reduce((lambda x, y: [i + j for i in x for j in y]), letters,['']) 
        
        
 class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        codec = {2:'abc', 3:'def', 4:'ghi',5:'jkl', 6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
       
        ans = ['']
        for d in list(digits):
            #if d in'23456789':
                ans = [prev+ch for prev in ans 
                            for ch in codec[int(d)]]
        return ans
                    
