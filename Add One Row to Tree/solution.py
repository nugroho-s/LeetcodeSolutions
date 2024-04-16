# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int, isRight = False) -> Optional[TreeNode]:
        if not root:
            if depth is 1:
                return TreeNode(val)
            return root
        if depth is 1:
            new_node = TreeNode(val, root if not isRight else None, root if isRight else None)
            return new_node
        new_left = self.addOneRow(root.left, val, depth - 1, False)
        new_right = self.addOneRow(root.right, val, depth - 1, True)
        root.left = new_left
        root.right = new_right
        return root
        
