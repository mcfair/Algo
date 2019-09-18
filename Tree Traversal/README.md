```python
def inorderTraversal(self, root):
    def inorder(root):
        if root:
            for x in inorder(root.left): yield x
            yield root
            for x in inorder(root.right): yield x

    return [x.val for x in inorder(root)]
```
