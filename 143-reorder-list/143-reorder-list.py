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
        slow = fast = head
        prev = None
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        if not prev: return head
        prev.next = None
        prev, cur, = None, slow
        
        while cur:
            nex = cur.next
            cur.next = prev
            prev = cur
            cur = nex
        p, q = head, prev
        
        while p.next and q.next:
            nextP = p.next
            nextQ = q.next
            p.next = q
            q.next = nextP
            p = nextP
            q = nextQ
        if q:
            p.next = q
        return head
        
            
        
        