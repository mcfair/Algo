"""
elegant slow/fast pointers
"""
def removeNthFromEnd(self, head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return head
"""
Value-Shifting - AC in 64 ms
Instead of really removing the nth node, I remove the nth value. I recursively determine the indexes (counting from back), 
then shift the values for all indexes larger than n, and then always drop the head.
""" 
def removeNthFromEnd(self, head, n):
    def index(node):
        if not node:
            return 0
        i = index(node.next) + 1
        if i > n:
            node.next.val = node.val
        return i
    index(head)
    return head.next

"""
Index and Remove - AC in 56 ms
In this solution I recursively determine the indexes again, but this time my helper function removes the nth node. 
It returns two values. The index, as in previous solution, and the possibly changed head of the remaining list.
"""
 
def removeNthFromEnd(self, head, n):
    def remove(head):
        if not head:
            return 0, head
        i, head.next = remove(head.next)
        return i+1, (head, head.next)[i+1 == n]
    return remove(head)[1]


