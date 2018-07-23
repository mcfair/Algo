class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head or m == n: return head
        
        #add dummy butter to head
        prev = ListNode(0)
        prev.next, head = head, prev
        
        mpt = npt = head
        for i in range(m-1):
            mpt = mpt.next
            
        for i in range(n):
            npt = npt.next
        
        endpt = npt.next
        npt.next = None 
             
            
        l, r = self.reverse(mpt.next)
        
        mpt.next = l
        r.next = endpt
  
        return head.next

    def reverse(self, head):
        l , r = None, head
        while r:
            l, r.next, r = r, l, r.next
        return l, head
    
    def printll(self, head):
        ret = ''
        while head:
            ret += str(head.val) +'->'
            head = head.next
        ret += '#'
        print ret
