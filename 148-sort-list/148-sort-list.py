# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        def getMid(head):
            if not head or not head.next:
                return head
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def merge(left, right):
            dummy = ListNode()
            p = dummy
            while left and right:
                if left.val < right.val:
                    p.next = left
                    left = left.next
                else:
                    p.next = right
                    right = right.next
                p = p.next
            p.next = left or right
            return dummy.next
        
        left = head
        right = getMid(head)
        tmp = right.next
        right.next = None
        right = tmp
        
        l = self.sortList(left)
        r = self.sortList(right)
        return merge(l, r)
        