class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(n):
            for n in graph[n]:
                if n not in seen:
                    seen.add(n)
                    dfs(n)


        seen = set()
        ans = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                ans += 1

        return ans

