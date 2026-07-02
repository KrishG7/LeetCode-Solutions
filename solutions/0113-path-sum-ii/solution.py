# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res=[]

        def backtrack(root, path):
            if not root:
                return []
            
            path.append(root.val)
            
            if not root.left and not root.right and sum(path) == targetSum:
                res.append(list(path))

            if backtrack(root.left, path) or backtrack(root.right, path):
                res.append(list(path))
                
            path.pop()

        backtrack(root, [])
        return res
