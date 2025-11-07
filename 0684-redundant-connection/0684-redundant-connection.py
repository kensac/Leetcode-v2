class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges) + 1)]
        
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
                return [node1, node2]