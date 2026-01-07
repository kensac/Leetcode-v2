# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def recurse(root):
            if not root:
                return (0, True)
            
            left = recurse(root.left)
            right = recurse(root.right)
            is_balanced = True

            if not left[1] or not right[1] or abs(left[0] - right[0]) > 1:
                is_balanced = False
            
            return (1 + max(left[0], right[0]), is_balanced)
        
        return recurse(root)[1]