```python
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None
       
class LinkedList(Object):
    def __init__(self, input=[]):
        self.head = self.tail = ListNode(None) 
        self.len = 0
        if input:
            self.createFromArray(input)
            
            
    def createFromArray(self,input):
        """create linked list from a python sequence, i.e. list, tuple"""
        self.head = self.tail = ListNode(None) 
        for x in input:
            self.tail.next = ListNode(x)
            self.tail = self.tail.next
        if input:
            self.len = len(input)
            self.head = self.head.next
            
    def removeDuplicatesFromSortedList(self):
         if not self.head or not self.head.next:
            return 
        
        slow = self.head
        fast = self.head.next
        
        while slow and fast:
            if fast.val ==slow.val:
                slow.next = fast.next  #skip fast node
                fast = slow.next
            else:
                slow = slow.next
                fast = fast.next
 
    def sort(self, inplace=False): 
        if not self.head: 
            return
        if not inplace:
            array = []
            curr = head
            while curr:
                array.append(curr.val)
                curr = curr.next
            array.sort()
            self.createFromArray(array)
        else:                              #sort inplace using insertion sort
            dummy = ListNode(None)
            dummy.next = self.head
            pre, cur = dummy, dummy.next
            while cur and cur.next:
                if cur.next.val >= cur.val:  #already sorted
                    cur = cur.next
                else:
                    while pre.next and pre.next.val < cur.next.val:  #scan from the beginning of the list
                        pre = pre.next
                    #found 'cur.next' is inbetween 'pre' and 'pre.next'
                    #so need to insert after pre
                    """
                    #verbose way
                    tmp = pre.next  #temporarily break the link
                    pre.next = cur.next
                    cur.next = cur.next.next  
                    pre.next.next = tmp
                    """
                    pre.next, cur.next, pre.next.next = cur.next, cur.next.next, pre.next
                    pre = dummy
             self.head = pre.next
                 
            
        
    def removeByValue(self, v):
        """remove all nodes with val v"""
        if not self.head or not v: return
        prev = ListNode(None) 
        prev.next = self.head
        curr = self.head
        self.head = prev              #to handle the case when first element needs to be removed
        while curr:
            if curr.val == v:         #find it
                prev.next = curr.next #skip/delete curr
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
         self.head = self.head.next
         
    def rotate(self, k,direction='right'):
         if not k or not self.len: return
         
         k %= self.len                 #also convert negative k to positive
         steps = self.len-k if direction=='right' else k
         
         self.tail.next = self.head
         for _ in range(steps):
            self.head = self.head.next
            self.tail = self.tail.next
         self.tail.next = None
         
    def deleteNode(self,node):
        """
        delete a specific node
        input is a ListNode object
        can't handle tail node
        """
        if node is not self.tail:
            node.val = node.next.val
            node.next = node.next.next
```
