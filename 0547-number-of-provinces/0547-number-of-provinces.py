class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        parent = [i for i in range(len(isConnected))]
        rank = [0 for _ in range(len(isConnected))]

        def union(x, y):
            x = find(x)
            y = find(y)

            if x == y:
                return

            if rank[x] < rank[y]:  # swap vars so x is greater and y is smaller
                x, y = y, x

            parent[y] = x
            if rank[x] == rank[y]:
                rank[x] += 1
            return

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j] == 1:
                    union(i, j)

        print(parent)

        return len(set([find(i) for i in range(len(isConnected))]))
