
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        dummy = ListNode('#');  # construct a dummy node
        dummy.next = head 

        pre = dummy           # set up pre and cur pointers
        cur = head
        while cur:
            if cur.next and cur.val == cur.next.val:
                # loop until cur point to the last duplicates
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                pre.next = cur.next  # propose the next for pre
                                     # this will be verified by next line
            else:
                pre = pre.next 
                
            cur = cur.next
        return dummy.next
        
        
#This solution doesn't assume it's sorted list.
#It's actually as fast as Method 1 above
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
            
        
        
        
