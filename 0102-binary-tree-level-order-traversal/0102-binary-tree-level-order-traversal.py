# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        res = [[root.val]]
        queue = deque([root])

        while queue:
            next_layer = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.left:
                    next_layer.append(cur.left)
                if cur.right:
                    next_layer.append(cur.right)
            if next_layer:
                queue.extend(next_layer)
                res.append([i.val for i in next_layer])
        return res
