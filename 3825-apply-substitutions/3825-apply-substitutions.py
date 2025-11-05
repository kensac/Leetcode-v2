class Solution:
    def applySubstitutions(self, replacements: List[List[str]], text: str) -> str:
        graph = {}
        subs = {}

        for key, value in replacements:
            graph[key] = list()
            subs[key] = value

        indegree = defaultdict(int)

        for key, value in subs.items():
            for char in value:
                if char in graph:
                    graph[key].append(char)
                    indegree[char] += 1

        queue = deque([key for key, value in graph.items() if indegree[key] == 0])
        print(graph, subs, indegree, queue)
        while queue:
            cur = queue.popleft()
            text = text.replace(f"%{cur}%", subs[cur])

            for neighbour in graph[cur]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        return text
