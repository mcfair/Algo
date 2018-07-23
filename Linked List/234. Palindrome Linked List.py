
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #find the middle while reverse the linked list
        if not head or not head.next:
            return True
        
        rev, slow, fast = None, head, head
        
        while fast and fast.next:
            fast = fast.next.next
            rev, slow , rev.next  = slow, slow.next, rev 
        
        #If the length of the linked list is odd
        if fast:
            slow = slow.next
        #Compare the reversed first half with the second half.
        while slow and rev.val == slow.val:
            slow = slow.next
            rev = rev.next
        return slow==None
