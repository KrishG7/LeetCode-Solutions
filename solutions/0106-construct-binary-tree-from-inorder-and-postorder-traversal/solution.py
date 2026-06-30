# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map = {val: i for i, val in enumerate(inorder)}
        
        def build(in_start, in_end, post_start, post_end):
            if in_start > in_end or post_start > post_end:
                return None
            
            # The root is the last element in the current postorder range
            root_val = postorder[post_end]
            root = TreeNode(root_val)
            
            # Find root in inorder
            in_root_idx = inorder_map[root_val]
            left_size = in_root_idx - in_start
            
            # Recursively build: 
            # Right subtree uses the end of postorder
            root.right = build(in_root_idx + 1, in_end, 
                               post_start + left_size, post_end - 1)
            
            # Left subtree comes before the right subtree in postorder
            root.left = build(in_start, in_root_idx - 1, 
                              post_start, post_start + left_size - 1)
            
            return root
            
        return build(0, len(inorder) - 1, 0, len(postorder) - 1)
