"""
Find the starting point of the cycle 

Consider the following linked list, where E is the cylce entry and X, the crossing point of fast and slow.
        H: head
        E: entry point of circle
        X: where slow and fast meet
        L: cycle length
                          X___
                         /     \
        H_______________E       \
                        \       /
                         \_____/   
        
    
        If fast and slow both start at head, when fast catches slow.
        Slow has traveled |HE|+|EX|+m*L and fast |HE|+|EX|+n*L. (have travelled m loops, n loops in the circle, respectively)
        Since fast is 2x speed of slow, and given the same time, fast has traveled 2x distanc. Therefore,
        2*(|HE|+|EX|+m*L) = |HE|+|EX|+n*L
        |HE|+|EX| = (n-2*m)*L, where (n-2*m) is some integer.
        |HE| = k*L - |EX|, where integer k>=1
        
        Thus if we have two pointers starting from head and X, respectively, they will definitely meet at E. 
"""

def detectCycle(self, head):

    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            walk = head #or we can just modify head
            while slow != walk:
                slow = slow.next
                walk = walk.next
            return slow

    return None
  
  
  
#reference: solution for LC141. Linked List Cycle (Check whether there is a cycle).
def hasCycle(self, head):
    if not head: return False
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next
        if slow==fast:
            return True
    return False
