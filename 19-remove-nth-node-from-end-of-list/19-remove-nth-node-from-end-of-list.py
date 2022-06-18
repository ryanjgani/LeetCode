# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev = None
        nextNode = None
        p = q = head
        count = 1
        while count < n:
            p = p.next
            count += 1
        while p.next:
            p = p.next
            prev = q
            q = q.next
        if not prev:
            head = head.next
        else:
            prev.next = q.next
        return head