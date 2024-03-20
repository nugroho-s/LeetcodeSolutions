# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # at node a, we need to insert list2, and then connect the end of list2 to the node at b
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        iter1 = list1
        b = b - a + 1
        while a-1 > 0:
            a -= 1
            iter1 = iter1.next
        contd = iter1.next
        iter1.next = list2
        l2end = list2
        while l2end.next:
            l2end = l2end.next
        while b > 0:
            b -= 1
            contd = contd.next
        l2end.next = contd
        return list1
