# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.root1_leaves = []
        self.root2_leaves = []

        def pre_order(root: Optional[TreeNode], leaves):
            if not root:
                return

            if not root.left and not root.right:
                leaves.append(root.val)

            pre_order(root.left, leaves)
            pre_order(root.right, leaves)
        
        pre_order(root1, self.root1_leaves)
        pre_order(root2, self.root2_leaves)

        return self.root1_leaves == self.root2_leaves