# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p = q = head
        while p and p.next:
            while p.next and p.val == p.next.val:
                p.next = p.next.next
            p = p.next
        return head