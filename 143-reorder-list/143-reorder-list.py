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
        while left and right:
            tmp1, tmp2 = left.next, right.next
            left.next = right
            right.next = tmp1
            left, right = tmp1, tmp2
        