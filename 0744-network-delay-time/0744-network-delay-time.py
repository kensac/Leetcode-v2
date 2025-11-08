class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_cost = 0
        visited = set()
        graph = defaultdict(list)
        for start, end, time in times:
            graph[start].append((end, time))

        queue = [(0, k)]

        while queue:
            cost, cur = heappop(queue)
            # print(cur, cost, graph[cur])
            if cur in visited:
                continue
            visited.add(cur)
            max_cost = max(max_cost, cost)
            for neighbour, increase in graph[cur]:
                heapq.heappush(queue, (cost + increase, neighbour))
        return max_cost if len(visited) == n else -1
