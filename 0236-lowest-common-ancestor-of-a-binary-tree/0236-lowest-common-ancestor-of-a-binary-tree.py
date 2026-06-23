# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        queue = deque([root])
        parent_map = {root: None}

        while queue:
            cur_node = queue.popleft()
            if cur_node.left:
                parent_map[cur_node.left] = cur_node
                queue.append(cur_node.left)
            
            if cur_node.right:
                parent_map[cur_node.right] = cur_node
                queue.append(cur_node.right)
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent_map[p]
        
        while q not in ancestors:
            q = parent_map[q]
        
        return q
