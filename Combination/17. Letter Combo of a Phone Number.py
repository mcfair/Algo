#DFS backtracking
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        codec = {2:'abc', 3:'def', 4:'ghi',5:'jkl', 6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
  
        def letterCombo(i):
            if i == 0:
                return []
            if i == 1:
                return list(codec[int(digits[0])])
            prefix = self.letterCombinations(digits[:i-1])
            additional = codec[int(digits[i-1])]
            return [pre + c for pre in prefix for c in additional]  
         
        return letterCombo(len(digits))

#Readable BFS
 class Solution(object):
    def letterCombinations(self, digits):
        if not digits: return []
        codec = {2:'abc', 3:'def', 4:'ghi',5:'jkl', 6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        
        ans = ['']
        for d in list(digits):
            tmp=[]
            for prev in ans:
                for ch in codec[int(d)]:
                    tmp.append(prev+ch) 
            ans=tmp
       
        return ans

#Reduce
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
        
        

                    
