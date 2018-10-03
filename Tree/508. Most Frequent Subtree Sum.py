class Solution(object):
    def findSum(self, node):
        if not node: return 0
        return node.val + self.findSum(node.left) + self.findSum(node.right)
    
    def dfs(self, node):
        if node:
            self.freq[self.findSum(node)] +=1
            self.dfs(node.left)
            self.dfs(node.right)
               
    def findFrequentTreeSum(self, root):
        if not root: return []
        
        self.freq = collections.defaultdict(int)
        self.dfs(root)
        maxfreq = max(self.freq.values())
        return [k for k, v in self.freq.items() if v==maxfreq]
