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
            stack.extend(reversed(p.children))
        return res
