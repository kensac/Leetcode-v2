class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(set)
        indegree = [0 for _ in range(numCourses)]

        # Create the Graph
        for course, prereq in prerequisites:
            graph[prereq].add(course)
            indegree[course] += 1

        # Set up Deque for topo sort
        queue = Deque([idx for idx in range(numCourses) if indegree[idx] == 0])
        result = []

        while queue:
            cur_course = queue.popleft()
            for neighbour in graph[cur_course]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

            result.append(cur_course)

        return result if len(result) == numCourses else []
