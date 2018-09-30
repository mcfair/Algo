class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """ 
        kv = collections.Counter(s)
        mid = [k for k, v in kv.iteritems() if v%2]
        if len(mid) > 1: return []
        
        mid = '' if not mid else mid[0]
        half =  ''.join([k * (v/2) for k, v in kv.iteritems()])
         
        n = len(half)
        ans = []
        visited = [False] * n
        
        def backtrack(tmp):
            if len(tmp) == n:
                cur = ''.join(tmp)
                ans.append(cur + mid + cur[::-1])
            else:
                for i in range(n):
                    
                    if visited[i]:
                        continue
                    #avoid duplication
                    if i-1 >= 0 and half[i] == half[i-1] and not visited[i-1]:
                        continue 
                    visited[i] = True
                    tmp.append(half[i])
                    backtrack(tmp)
                    visited[i] = False
                    tmp.pop()#try next one

        backtrack([])
        return ans
