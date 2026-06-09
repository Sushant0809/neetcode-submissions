from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        x = [-1,1,0,0]
        y = [0,0,-1,1]

        m = len(grid)
        n = len(grid[0])

        

        def valid(i,j):
            if i<0 or i>=m or j<0 or j>=n:
                return False
            return True

        queue = deque()
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append([i,j])
                    
        
        while queue:
            node = queue.popleft()
            r = node[0]
            c = node[1]

            for k in range(4):
                row = r + x[k]
                col = c + y[k]

                if valid(row,col):
                    if grid[row][col]==2147483647:
                        grid[row][col] = 1+grid[r][c]
                        queue.append([row,col])
                        
                    



        