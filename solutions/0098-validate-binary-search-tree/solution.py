# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, low, high):
            if not node:
                return True

            # Check current node value against constraints
            if not (low < node.val < high):
                return False

            # Recurse: left subtree must be < node.val, right must be > node.val
            return validate(node.left, low, node.val) and validate(
                node.right, node.val, high
            )

        return validate(root, float("-inf"), float("inf"))

