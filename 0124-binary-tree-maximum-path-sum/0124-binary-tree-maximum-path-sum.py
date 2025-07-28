# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = float("-inf")

        def recurse(root: TreeNode) -> int:
            if not root:
                return 0
            left = max(0, recurse(root.left))
            right = max(0, recurse(root.right))
            self.res = max(self.res, root.val + left + right)

            return root.val + max(right, left)

        recurse(root)
        return self.res
