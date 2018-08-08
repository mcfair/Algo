#coin change - unlimited coins -  but this is backtracking not counting numbers
#it asks for all combinations

#naive DFS
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        def find(target, bag):
    
            if target ==0:
                bag = tuple(sorted(bag))
                if bag not in combo:
                    combo.append(bag)
                return 
            for c in candidates :
                if target-c>=0:
                    find(target-c,  bag+[c])
            
            
        combo = []
        find(target,  [])
        return combo

#another way to strictly removed the duplicates without compare
#when searching with for loop, never check the node backward.
  
 class Solution(object):
    def combinationSum(self, candidates, target):
            """
            :type candidates: List[int]
            :type target: int
            :rtype: List[List[int]]
            """
            def dfs(candidates, target, path):
                if target < 0:
                    return
                if target == 0:
                    res.append(path)
                    return
                for i in xrange(len(candidates)):
                    dfs(candidates[i:],target-candidates[i],path+[candidates[i]] )                
            res = []
            dfs(candidates, target,[] )
            return res

    
#passing index instead of array
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        combo = []
        def dfs(target,k,bag):
            if target<0: return
            if target==0:         
                combo.append(bag)
                return
            for i, c in enumerate(candidates[k:],k): 
                dfs(target-c, i, bag+[c])
        
        dfs(target, 0, [])
        return combo
