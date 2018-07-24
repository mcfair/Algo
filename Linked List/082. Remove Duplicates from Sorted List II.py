 
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #naive way is use a Counter, two pass O(n)
        if not head or not head.next:
            return head
        
        counts = collections.defaultdict(int)
        p = head
        #O(n)
        while p:
            counts[p.val] +=1
            p = p.next
      
        slow = ListNode('#')
        slow.next = fast = head
        head = slow
        
        #O(n)
        while fast:
            if counts[fast.val]>1:
                slow.next = fast.next
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
                
        return head.next
            
        
        
        
