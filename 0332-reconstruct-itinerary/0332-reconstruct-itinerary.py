class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = defaultdict(list)

        tickets.sort(reverse=True)
        for start, dest in tickets:
            graph[start].append(dest)

        stack = ["JFK"]
        new_itinerary = []

        while stack:
            if graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop())
            else:
                new_itinerary.append(stack.pop())

        return new_itinerary[::-1]
