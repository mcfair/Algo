#Iterative way
class Solution(object):
    def reverseList(self, head):
 
        l , r = None, head
        while r:
            l,  r,  r.next = r,   r.next, l 
        return l




#Recursive way

class Solution(object):
    def reverseList(self, head):
 
        return self._reverse(head)

    def _reverse(self, cur, prev=None):
        if not cur:
            return prev
        nxt = cur.next
        cur.next = prev
        return self._reverse(nxt, cur)
