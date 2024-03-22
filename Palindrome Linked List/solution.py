# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        iter1 = head
        head2 = ListNode(head.val)
        prev2 = ListNode(head.val)
        while iter1.next:
            head2 = ListNode(iter1.next.val, prev2)
            prev2 = head2
            iter1 = iter1.next
        return head2

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        reversed_list = self.reverseList(head)
        while head:
            if head.val is not reversed_list.val:
                return False
            head = head.next
            reversed_list = reversed_list.next
        return True
        
