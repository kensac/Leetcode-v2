class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Model as graph
        graph = defaultdict(set)
        indegree = [0 for _ in range(numCourses)]
        for prev, cur in prerequisites:
            graph[prev].add(cur)
            indegree[cur] += 1


        queue = deque([idx for idx, val in enumerate(indegree) if val == 0])

        while queue:
            cur = queue.popleft()
            for neighbour in graph[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return all([True if val==0 else False for val in indegree])