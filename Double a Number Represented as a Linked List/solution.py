# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solution for reverse linked list
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

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head = self.reverseList(head)
        i = head
        c = 0
        while i:
            d = i.val * 2 + c
            c = d // 10
            i.val = d % 10
            prev = i
            i = i.next
        if c is not 0:
            prev.next = ListNode(c)
        return self.reverseList(head)
