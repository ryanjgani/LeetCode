# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        cur = slow.next
        _next = None
        slow.next = None
        while cur:
            _next = cur.next
            cur.next = prev
            prev = cur
            cur = _next
        left, right = head, prev
        dummy = ListNode()
        p = dummy
        while left and right:
            p.next = left
            left = left.next
            p = p.next
            p.next = right
            right = right.next
            p = p.next
        p.next = left or None
        return dummy.next