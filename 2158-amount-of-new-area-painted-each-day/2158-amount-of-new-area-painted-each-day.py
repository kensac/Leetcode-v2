class Solution:
    def amountPainted(self, paint: List[List[int]]) -> List[int]:
        max_end = max(end for _, end in paint)
        parent = list(range(max_end + 1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        ans = []
        for start, end in paint:
            work = 0
            x = find(start)

            while x < end:
                work += 1
                parent[x] = find(x + 1)

                x = find(x)
            ans.append(work)

        return ans
