#Recursive solution is trivial
class RecursiveSolution(object):
    def preorder(self, root):
        if not root: return []
        
        res=[root.val]
        for i in root.children:
            res += self.preorder(i)
        return res
        
 #Iterative Solution
 class IterativeSolution(object):
    def preorder(self, root):
        if not root: return []
        stack = [root]
        res = []
        while stack:
            p=stack.pop()
            res.append(p.val)
            for i in reversed(range(len(p.children))): 
                stack.append(p.children[i])
        return res
