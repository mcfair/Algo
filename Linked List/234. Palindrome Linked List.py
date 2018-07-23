#key is reversing the linked list while looking for middle point
#reverse is classical 3-way swap: l, l.next, r = r, l, r.next
#find middel point is classical slow/fast pointers
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        
        if not head or not head.next:
            return True
        
        left, slow, fast = None, head, head
        
        #find the middle while reverse the linked list
        while fast and fast.next:
            fast = fast.next.next
            left,  left.next, slow   = slow,  left , slow.next
        
  
        #If the length of the linked list is odd
        if fast:
            slow = slow.next
            
        #Compare the reversed left half ('left') with the right half ('slow').
        while slow and left.val == slow.val:
            slow = slow.next
            left = left.next
        return left == None
    
    def printll(self, head):
        ret = ''
        while head:
            ret += str(head.val) +'->'
            head = head.next
        ret += '#'
        print ret
