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
        #if hitting the end of list (None), return its prev (new head)
        if not cur:
            return prev
        #save next node for recursion
        nxt = cur.next
        #for the purpose of reverse, let cur.next point to prev
        cur.next = prev
        return self._reverse(nxt, cur)
