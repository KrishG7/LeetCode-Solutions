# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []

        def dfs(node, current_path):
            if not node:
                return

            new_path = current_path + str(node.val)

            if not node.left and not node.right:
                paths.append(new_path)
            else:
                if node.left:
                    dfs(node.left, new_path + "->")
                if node.right:
                    dfs(node.right, new_path + "->")

        dfs(root, "")
        return paths

