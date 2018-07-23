class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
         
        reversed = self.reverse(head)
        reversed.val, carry  = (reversed.val+1)%10, (reversed.val+1)/10
        r = reversed
     
        while carry:
          
            if r.next:
                r = r.next
                r.val, carry = (r.val+carry)%10, (r.val+carry)/10
                #when calculate remainder and carry, update the same time to avoid saving r.val as tmp
            else:
                r.next = ListNode(carry)
                carry = 0
    
        return self.reverse(reversed)
    
    #LC206. Reverse Linked List
    #Remember the animation and squence of 3-way swapping "l, r.next, r"
    def reverse(self,head):
        l , r = None, head
        while r:
            l,  r.next,  r = r,   l,  r.next
        return l
