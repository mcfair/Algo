# https://leetcode.com/problems/path-sum-iii/discuss/91892/Python-solution-with-detailed-explanation
"""
Double DFS - elegant
similar to the way we write preorder traversal
Time = O(nlogn) if balanced tree, else worst case O(n^2)
"""
#Find number of paths
class SolutionFindNumberOfPaths(object):
    def find_paths(self, root, target):
        if root:
            return int(root.val == target) + \
                   self.find_paths(root.left, target-root.val) + \
                   self.find_paths(root.right, target-root.val)
        return 0

    def pathSum(self, root, sum):
 
        if root:
            return self.find_paths(root, sum) + \
                   self.pathSum(root.left, sum) + \
                   self.pathSum(root.right, sum)
        return 0
      
#Find all possible paths
class SolutionFindAllPaths(object):
    def find_paths(self, root, target, path): 
        if not root: 
            return 
        if root.val == target:
            self.paths.append(path+[root.val])
        self.find_paths(root.left, target-root.val, path+[root.val]) 
        self.find_paths(root.right, target-root.val,path+[root.val])
        
    def preorder(self, root, sum):
        if root:
            self.find_paths(root, sum, [])
            self.preorder(root.left, sum) 
            self.preorder(root.right, sum)
            
    def pathSum(self, root, sum):
        self.paths = []
        self.preorder(root, sum)
        return self.paths
      
"""
Two Sum Method: Optimized Solution

- A more efficient implementation uses the Two Sum idea. It uses a hash table (extra memory of order N). 
With more space, it gives us an O(N) complexity.
- As we traverse down the tree, at an arbitrary node N, we store the sum from root to this node N in hash-table. 
prefixsum(root->N) = prefixsum(root->parent_of_N) + N.val
- Now at a grand-child of N, say G, we can compute the sum from the root until G since we have the prefix_sum until this grandchild available.
We pass in our recursive routine.
- How do we know if we have a path of target sum which ends at this grand-child G? Say there are multiple such paths that end at G and say they start at A, B, C where A,B,C are predecessors of G. Then sum(root->G) - sum(root->A) = target. Similarly sum(root->G)-sum(root>B) = target. Therefore we can compute the complement at G as sum_so_far+G.val-target and look up the hash-table for the number of paths which had this sum
- Now after we are done with a node and all its grandchildren, we remove it from the hash-table. This makes sure that the number of complement paths returned always correspond to paths that ended at a predecessor node.
"""
class Solution:
    def pathSum(self, root, target):
        self.ans = 0
        cache = collections.defaultdict(int)
        cache[0] = 1 #target = 0 has a least 1 path, which is [None]
        
        def dfs(node, cur_sum):
          if node:
              cur_sum += node.val
              self.ans += cache[cur_sum - target]

              cache[cur_sum] += 1
              dfs(node.left, cur_sum)
              dfs(node.right, cur_sum)
              cache[cur_sum] -= 1
            
        dfs(root, 0)
        return self.ans
