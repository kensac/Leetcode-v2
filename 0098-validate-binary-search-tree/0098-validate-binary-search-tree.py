# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def inOrder(root):
            #print(root, self.prev)
            if not root:
                return True
            if not inOrder(root.left):
                return False
            if self.prev >= root.val:
                return False
            self.prev = root.val

            return inOrder(root.right)
            
        self.prev = float("-inf")
        return inOrder(root)
