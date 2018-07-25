class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ascending order tells you its in level order (BFS order)
        # idea is to reconstruct the tree using dict
 
        tree = collections.defaultdict(int)
        for x in nums:
            lvl, pos, val = self.parseDigits(x)
            tree[lvl, pos] = val
            
        ret = [0]
        def traverse(lvl,pos, pathsum):
            left = lvl+1, pos*2
            right = lvl+1, pos*2+1
            pathsum += tree[lvl,pos]
            if left not in tree and right not in tree:
                ret[0]+=pathsum
                return 
            
            if left in tree: 
                traverse(lvl+1, pos*2 , pathsum)
            if right  in tree: 
                traverse(lvl+1, pos*2+1,pathsum)
        
        traverse(0,0,0)    
        return ret[0]
            
    def parseDigits(self, x):
        level, x = divmod(x, 100)
        pos, val = divmod(x, 10)
         
        return level-1, pos-1, val
