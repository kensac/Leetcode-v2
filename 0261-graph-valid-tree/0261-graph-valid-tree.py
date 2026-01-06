class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != (n -1):
            return False
            
        parent = [i for i in range(n)]

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]
        
        def union(node1, node2):
            node1 = find(node1)
            node2 = find(node2)
            if node1 == node2:
                return False
            
            parent[node1] = node2

            return True

        for start, end in edges:
            if not union(start, end):
                return False

        return True            
