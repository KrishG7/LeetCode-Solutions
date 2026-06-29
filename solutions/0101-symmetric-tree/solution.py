# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left, root.right)
    
    def isMirror(self, leftNode, rightNode):
        # 1. Both nodes are None: Symmetric
        if not leftNode and not rightNode:
            return True
        # 2. Only one is None or values differ: Not symmetric
        if not leftNode or not rightNode or leftNode.val != rightNode.val:
            return False
        
        # 3. Check outer pairs and inner pairs recursively
        return self.isMirror(leftNode.left, rightNode.right) and \
               self.isMirror(leftNode.right, rightNode.left)
