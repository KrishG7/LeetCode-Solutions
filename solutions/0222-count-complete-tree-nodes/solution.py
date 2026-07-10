# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_node = root
        left_depth = 0
        while left_node:
            left_depth += 1
            left_node = left_node.left

        right_node = root
        right_depth = 0
        while right_node:
            right_depth += 1
            right_node = right_node.right

        #  If the left_depth equals the right_depth, you are looking at a perfectly full binary tree. The total number of nodes can be calculated instantly using math: (2^depth )- 1
        if left_depth == right_depth:
            return (2**left_depth) - 1

        # If the depths are different, the tree is not perfectly full. In that case, you recursively ask for the node count of the left and right subtrees and add 1 (for the current root)
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

