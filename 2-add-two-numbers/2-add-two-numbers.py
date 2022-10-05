# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p, q = l1, l2
        dummy = ListNode(-1)
        r = dummy
        digits = rem = 0
        while p and q:
            count = p.val + q.val + rem
            rem = count // 10
            count = count % 10
            newNode = ListNode(count)
            r.next = newNode
            p, q, r = p.next, q.next, r.next
            digits += 1
        z = p or q
        while z:
            count = z.val + rem
            rem = count // 10
            count = count % 10
            newNode = ListNode(count)
            r.next = newNode
            z, r = z.next, r.next
        if rem:
            newNode = ListNode(rem)
            r.next = newNode
            
        return dummy.next
            
        