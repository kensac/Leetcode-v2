class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        parent = [i for i in range(n)]

        def find(node):
            while node != parent[node]:
                node = parent[node]
            return node

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return False
            parent[p1] = p2
            return True

        for node1, node2 in edges:
            if not union(node1, node2):
                return False

        return True
