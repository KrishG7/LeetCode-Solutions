"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None
        
        leftmost=root

        while leftmost.left:
            curr=leftmost

            while curr:
                # 1. Connect the left child to the right child (siblings)
                curr.left.next=curr.right

                # 2. Connect the right child to the next neighbor's left child (cousins)
                if curr.next:
                    curr.right.next=curr.next.left
                
                # Move sideways to the next node on this level
                curr=curr.next
            
            # Once the level is fully connected, move down to the next level
            leftmost=leftmost.left
        
        return root
