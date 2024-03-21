# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        iter1 = head
        prev1 = None
        next1 = head
        while iter1.next:
            next1 = iter1.next
            iter1.next = prev1
            prev1 = iter1
            iter1 = next1
        iter1.next = prev1
        return iter1
