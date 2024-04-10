
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        i1 = list1
        i2 = list2
        head = None
        if i1.val <= i2.val:
            head = i1
            i1 = i1.next
        else:
            head = i2
            i2 = i2.next
        mi = head
        while i1 or i2:
            if not i1:
                mi.next = i2
                break
            if not i2:
                mi.next = i1
                break
            if i1.val <= i2.val:
                mi.next = i1
                i1 = i1.next
            else:
                mi.next = i2
                i2 = i2.next
            mi = mi.next
        return head
