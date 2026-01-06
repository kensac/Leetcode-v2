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
        old_to_new = {}
        if not node:
            return
        
        queue = deque([node])
        while queue:
            cur = queue.popleft()
            old_to_new[cur] = Node(cur.val)

            for neighbor in cur.neighbors:
                if neighbor not in old_to_new:
                    queue.append(neighbor)
        
        for key, value in old_to_new.items():
            for neighbor in key.neighbors:
                value.neighbors.append(old_to_new[neighbor])
        
        return old_to_new[node]