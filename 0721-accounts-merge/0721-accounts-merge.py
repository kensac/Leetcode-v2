class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        owner = {}
        size = {}

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(u, v):
            u, v = find(u), find(v)

            if u == v:
                return

            if size[u] < size[v]:
                u, v = v, u

            parent[v] = u
            size[u] += size[v]

        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                if email not in parent:
                    parent[email] = email
                    size[email] = 1
                    owner[email] = name

            first = acc[1]
            for email in acc[2:]:
                union(first, email)

        union_dict = defaultdict(list)
        for email in parent:
            root = find(email)
            union_dict[root].append(email)

        result = []
        for root, email in union_dict.items():
            result.append([owner[root]] + sorted(email))
        return result
