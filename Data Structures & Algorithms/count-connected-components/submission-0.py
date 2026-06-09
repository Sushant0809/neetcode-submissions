class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        seen = set()

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        def dfs(node):
            seen.add(node)

            for ele in adj[node]:
                if ele not in seen:
                    dfs(ele)
        
        count = 0

        for i in range(n):
            if i not in seen:
                dfs(i)
                count+=1
        
        return count
