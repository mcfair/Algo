# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return []
        if len(lists)==1: return lists[0]
        
        ret= pointer = ListNode(None)
        q = []
        for head in lists:
            if head:
                heapq.heappush(q,(head.val, head))
        while q:
            _, node = heapq.heappop(q)
            pointer.next = node
            pointer = pointer.next
            if node.next:
                heapq.heappush(q, (node.next.val, node.next))
            
        return ret.next        
