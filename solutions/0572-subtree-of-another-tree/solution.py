# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        def check(node, subnode):
            if not node and not subnode:
                return True
            if not node or not subnode:
                return False
            if node.val != subnode.val:
                return False
            return check(node.left, subnode.left) and check(node.right, subnode.right)

        if check(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

