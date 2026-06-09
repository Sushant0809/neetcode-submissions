from collections import deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        if len(edges)!=n-1:
            return False

        adj = [[] for _ in range(n)]

        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        seen = set()
        queue = deque()
        queue.append(0)
        seen.add(0)

        while queue:
            node = queue.popleft()
            for ele in adj[node]:
                if ele not in seen:
                    seen.add(ele)
                    queue.append(ele)
        
        return len(seen)==n






        

        