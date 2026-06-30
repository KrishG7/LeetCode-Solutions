# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        # 1. Get the total length of the linked list
        size = 0
        curr = head
        while curr:
            size += 1
            curr = curr.next
            
        # 2. Use a nonlocal pointer to track the current list node
        self.curr_node = head
        
        def build_bst(left, right):
            if left > right:
                return None
            
            mid = (left + right) // 2
            
            # Recursively build the left subtree
            left_child = build_bst(left, mid - 1)
            
            # Create the root node using the current list value
            root = TreeNode(self.curr_node.val)
            root.left = left_child
            
            # Advance the list pointer
            self.curr_node = self.curr_node.next
            
            # Recursively build the right subtree
            root.right = build_bst(mid + 1, right)
            
            return root
            
        return build_bst(0, size - 1)
        
