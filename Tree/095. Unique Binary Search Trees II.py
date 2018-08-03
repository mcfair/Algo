class Solution(object):
    def generateTrees(self, n):
        if n < 1: return []
        cache = {}
        
        def generate(first, last):
            #one smart line to handle cases of root==last, root+1>last
            if first > last: return [None] 
            if (first, last) in cache: return cache[first, last]
            trees = []
            for root in range(first, last+1):
                for left in generate(first, root-1):
                    for right in generate(root+1, last):
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees.append(node)
                        
            cache[first, last] = trees
            return trees
        
        return generate(1, n)
    
    
