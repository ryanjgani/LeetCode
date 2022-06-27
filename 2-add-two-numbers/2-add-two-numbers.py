# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = []
        num2 = []
        while l1:
            num1.append(str(l1.val))
            l1 = l1.next
        while l2:
            num2.append(str(l2.val))
            l2 = l2.next
        num1 = int("".join(num1[::-1]))
        num2 = int("".join(num2[::-1]))
        res = str(num1 + num2)
        res = res[::-1]
        head = ListNode(int(res[0]))
        p = head
        for i in range(1, len(res)):
            q = ListNode(int(res[i]))
            p.next = q
            p = q
        return head
        
        