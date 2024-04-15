# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode], num = 0) -> int:
        cur = num * 10 + root.val
        if not root.right and not root.left:
            return cur
        sum_left = self.sumNumbers(root.left, cur) if root.left else 0
        sum_right = self.sumNumbers(root.right, cur) if root.right else 0
        return sum_left + sum_right
