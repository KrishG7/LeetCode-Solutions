# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def backtrack(root, path):
            if not root:
                return False

            path.append(root.val)

            if not root.left and not root.right and sum(path) == targetSum:
                return True

            if backtrack(root.left, path) or backtrack(root.right, path):
                return True

            path.pop()
            return False

        return backtrack(root, [])

