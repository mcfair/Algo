 
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        
        slow = head
        fast = head.next
        
        while slow and fast:
            if fast.val ==slow.val:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
        return head
            
