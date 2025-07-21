# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        # The idea is to have the parent of every node all the way to the top
        # then using the target nodes, store all the parents we see for the first
        # and use the first parent of the other nodes
        # O(n), O(n)
        parent_map = {}
        def parent_mapper(node, parent):
            if not node:
                return
            parent_map[node] = parent
            parent_mapper(node.left, node)
            parent_mapper(node.right, node)
        parent_mapper(root, None)

        seen = set()
        cur = q
        while cur:
            seen.add(cur)
            cur = parent_map[cur]

        cur = p
        while cur and cur not in seen:
            cur = parent_map[cur]

        return cur
