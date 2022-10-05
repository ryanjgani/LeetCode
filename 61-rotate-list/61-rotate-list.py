# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        p = head
        while p:
            p = p.next
            length += 1
        if not k or length in (0, 1) or not k % length: return head
        k = k % length
        p = q = head
        for i in range(k):
            p = p.next
        while p.next:
            p, q = p.next, q.next
        newHead = q.next
        q.next = None
        p.next = head
        return newHead
        