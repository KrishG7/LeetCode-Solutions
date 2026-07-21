"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: "Node") -> List[int]:

        res = []
        def func(node):
            if not node :
                return 
            res.append(node.val)
            for child in node.children :
                func(child)
        func(root)
        return res


        # if not root:
        #     return []

        # res = [root.val]

        # for child in root.children:
        #     res.extend(self.preorder(child))

        # return res

