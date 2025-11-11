class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        heapify(logs)
        parent = [i for i in range(n)]

        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            p1 = find(node1)
            p2 = find(node2)

            if p1 == p2:
                return False

            parent[p1] = p2

            return True

        connected_components = n
        while logs:
            cur_time, f1, f2 = heappop(logs)
            if union(f1, f2):
                connected_components -= 1
            if connected_components == 1:
                return cur_time
        
        return -1
