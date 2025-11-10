class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: List[int], informTime: List[int]
    ) -> int:
        graph = defaultdict(list)
        for i, m in enumerate(manager):
            if m == -1:
                continue
            graph[m].append((informTime[m], i))
        res = 0
        seen = set()
        pq = [(0, headID)]

        while pq:
            cur_weight, cur = heappop(pq)
            if cur in seen:
                continue
            seen.add(cur)
            res = max(res, cur_weight)
            for sub_weight, sub in graph[cur]:
                heappush(pq, (cur_weight + sub_weight, sub))
            #print(pq)
        return res
