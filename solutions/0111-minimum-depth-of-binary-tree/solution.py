# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # 1. If it's a leaf node (no children), depth is 1
        if not root.left and not root.right:
            return 1
        
        # 2. If left child is missing, we MUST go right
        if not root.left:
            return self.minDepth(root.right) + 1
            
        # 3. If right child is missing, we MUST go left
        if not root.right:
            return self.minDepth(root.left) + 1
            
        # 4. If both children exist, take the minimum of the two paths
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
