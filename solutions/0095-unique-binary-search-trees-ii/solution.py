# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def buildTrees(start,end):
            if (start>end):
                return [None]
            all_trees=[]

            for i in range(start,end+1):
                left_trees=buildTrees(start,i-1)
                right_trees=buildTrees(i+1,end)

                for l in left_trees:
                    for r in right_trees:
                        current_root=TreeNode(i)
                        current_root.left = l
                        current_root.right = r
                        all_trees.append(current_root)
            
            return all_trees

        return buildTrees(1, n)
