class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0 for _ in range(numCourses)]
        for course, requirement in prerequisites:
            graph[requirement].append(course)
            indegree[course] += 1
        
        queue = Deque([i for i in range(numCourses) if indegree[i] == 0])

        while queue:
            cur_course = queue.popleft()
            
            for course in graph[cur_course]:
                indegree[course] -= 1
                if indegree[course] == 0:
                    queue.append(course)
        
        return all(i == 0 for i in indegree)
