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
    
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast_ptr = head
        slow_ptr = head
        while fast_ptr and fast_ptr.next:
            fast_ptr = fast_ptr.next.next if fast_ptr.next else fast_ptr.next
            slow_ptr = slow_ptr.next
        mid = slow_ptr.next
        slow_ptr.next = None
        rev_ptr = self.reverseList(mid)
        ptr = head
        while ptr and rev_ptr:
            temp = ptr.next
            temp2 = rev_ptr.next
            ptr.next = rev_ptr
            rev_ptr.next = temp
            ptr = temp
            rev_ptr = temp2
