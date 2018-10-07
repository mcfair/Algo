#Stephan add any number of lists
def addTwoNumbers(self, l1, l2):
    addends = [l1, l2]
    dummy = res = ListNode(0)
    carry = 0
    while addends or carry:
        carry += sum(a.val for a in addends)
        addends = [a.next for a in addends if a.next]
        res.next =  ListNode(carry % 10)
        res = res.next
        carry /= 10
    return dummy.next

#concise add two lists
def addTwoNumbers(self, l1, l2):
    dummy = cur = ListNode(0)
    carry = 0
    while l1 or l2 or carry:
        if l1:
            carry += l1.val
            l1 = l1.next
        if l2:
            carry += l2.val
            l2 = l2.next
        cur.next = ListNode(carry%10)
        cur = cur.next
        carry //= 10
    return dummy.next

#my verbose implementation
def addTwoNumbers(self, l1, l2):
 
    head = res = ListNode(None)
    carry = 0
    while l1 or l2:
        res.next = ListNode(0)
        res = res.next
        if not l1:
            addition = l2.val+carry
        elif not l2:
            addition = l1.val+carry
        else:
            addition = l1.val+l2.val+carry
        carry, res.val = divmod(addition, 10)

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    if carry>0:
        res.next= ListNode(carry)

    return head.next
