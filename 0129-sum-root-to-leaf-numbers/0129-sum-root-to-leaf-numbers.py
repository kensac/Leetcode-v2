# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.dfs(root, [])
        return self.res
    
    def dfs(self, node, chain):
        if not node:
            return
        
        chain.append(str(node.val))
        if not node.right and not node.left:
            self.res += int("".join(chain))
        
        self.dfs(node.left, chain)
        self.dfs(node.right, chain)
        chain.pop()