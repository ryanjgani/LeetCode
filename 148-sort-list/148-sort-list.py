# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(h1, h2):
            dummy = ListNode(-1)
            p = dummy
            while h1 and h2:
                if h1.val < h2.val:
                    p.next = h1
                    h1 = h1.next
                    p = p.next
                else:
                    p.next = h2
                    h2 = h2.next
                    p = p.next
            p.next = h1 or h2
            return dummy.next
                
        
        def mergeSort(head):
            if not head.next:
                return head
            
            dummy = ListNode(-1, head)
            slow = fast = dummy
            while fast and fast.next:
                fast = fast.next.next
                slow = slow.next
            right = mergeSort(slow.next)
            slow.next = None
            left = mergeSort(head)
            return merge(left, right)
        if not head: return None
        return mergeSort(head)
            
        
        