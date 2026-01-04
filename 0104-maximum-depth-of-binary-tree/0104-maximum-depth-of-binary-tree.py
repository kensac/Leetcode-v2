# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root)
        return self.res

    def dfs(self, root, cur_depth = 0):
        if not root:
            return
        cur_depth += 1
        self.res = max(cur_depth, self.res)
        self.dfs(root.left, cur_depth)
        self.dfs(root.right, cur_depth)
    
