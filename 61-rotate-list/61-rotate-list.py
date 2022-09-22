# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        p = head
        count = 0
        while p:
            count += 1
            p = p.next
        if k == 0 or count in (0, 1): return head
        k = k % count
        if k == 0 or count in (0, 1): return head

        p = q = head
        for i in range(k):
            p = p.next
        while p.next:
            p = p.next
            q = q.next
        newHead = q.next
        q.next = None
        p.next = head
        return newHead
        
