def addTwoNumbers(self, l1, l2):

    if not l1 or not l2:
        return l1 or l2

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
