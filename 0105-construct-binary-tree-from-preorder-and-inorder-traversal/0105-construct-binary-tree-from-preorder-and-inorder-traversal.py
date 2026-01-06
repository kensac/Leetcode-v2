# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def builder(preorder, inorder):
            if not preorder or not inorder:
                return None

            root_val = preorder.pop(0)
            idx = inorder.index(root_val)
            root = TreeNode(val=root_val)
            
            root.left = builder(preorder, inorder[:idx])
            root.right = builder(preorder, inorder[idx + 1 :])

            return root

        return builder(preorder, inorder)
