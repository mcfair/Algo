"""
The algorithm is called "Tortoise and hare".
"""
#standard slow and fast pointers (aka slow Tortoise and fast Hare)
def hasCycle(self, head):
    if not head or not head.next:
        return False

    slow = head
    fast = head.next
    while slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False
    
#cleaner version
def hasCycle(self, head):
    if not head: return False
    slow = fast = head
    while slow.next and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False
 
#use try/except    
def hasCycle(self, head):
    try:
        slow = head
        fast = head.next
        while slow is not fast:
            slow = slow.next
            fast = fast.next.next
        return True
    except:
        return False
