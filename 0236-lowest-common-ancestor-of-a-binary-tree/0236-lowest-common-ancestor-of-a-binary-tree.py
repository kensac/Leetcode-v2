# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None

        def recurse(node):
            if not node:
                return False
            
            left = recurse(node.left)
            right = recurse(node.right)
            if (left and right) or ((left or right) and (node == p or node == q)):
                self.res = node
            if node == p or node == q:
                return True
            return left or right
        
        if root == q or root == q:
            return root
        recurse(root)
        return self.res