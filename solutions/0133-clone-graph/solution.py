"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        # Our Hash Map to track visited nodes and their clones
        clones = {}
        
        def dfs(curr_node):
            # Base Case: If we've already cloned this node, just return the clone!
            if curr_node in clones:
                return clones[curr_node]
                
            # 1. Create the clone (only copying the value for now)
            clone = Node(curr_node.val)
            
            # 2. Add it to our dictionary immediately before we check neighbors
            clones[curr_node] = clone
            
            # 3. Recursively clone all neighbors and add them to our new clone's list
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            # 4. Return the fully built clone
            return clone
            
        # Kick off the DFS starting with the given node
        return dfs(node)
        
