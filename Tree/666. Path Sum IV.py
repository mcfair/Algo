class Solution(object):
    def pathSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # ascending order tells you its in level order (BFS order)
        # and in each layer it's sorted from left to right
        # idea is to reconstruct the tree while adding layers by layers
 
        tree = [[0]]
        for x in nums:
            lvl, pos, val, parent, isRightLeaf = self.parseDigits(x)
            if lvl > len(tree) -1:  
                tree.append(['']*2**lvl)
            tree[lvl][pos] = val 
            
        prev = tree[0]
  
        for level in tree[1:]:
            for i in range(0, len(level), 2):
                #i/2 is parent index
        
                left , right = level[i], level[i+1]
                if left is '' and   right is '':
                    level[i+1] = prev[i/2]
                if left is not '':
                    level[i] +=prev[i/2]
                if right is not '':
                    level[i+1] +=prev[i/2]
       
            prev = level
        return sum(filter(None, prev))
                
                
    def parseDigits(self, x):
        level, x = divmod(x, 100)
        pos, val = divmod(x, 10)
        isRightLeaf = (pos-1)%2
        parent = (pos-1)//2
        return level-1, pos-1, val, parent, isRightLeaf

    
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
