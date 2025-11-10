# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(
        self, root: Optional[TreeNode], target: int
    ) -> Optional[TreeNode]:

        def is_leaf(node: TreeNode):
            if not node.left and not node.right and node.val == target:
                return True
            return False

        def dfs(node):
            if not node:
                return True

            left_delete = dfs(node.left)
            if left_delete:
                node.left = None

            right_delete = dfs(node.right)
            if right_delete:
                node.right = None

            return is_leaf(node)

        dfs(root)
        if is_leaf(root):
            return None
        return root
