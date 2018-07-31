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
