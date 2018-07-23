#Iterative way
class Solution(object):
    def reverseList(self, head):
        # remember those 4 lines!
        l , r = None, head
        while r:
            l,  r.next,  r = r,  l,  r.next
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
