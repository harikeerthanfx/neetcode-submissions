class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        count = 0
        visited = set()
        rows, cols = len(grid),len(grid[0])

        def bfs(a,b):
            q = collections.deque();
            q.append((a,b))
            directions = [(1,0),(0,1),(-1,0),(0,-1)]

            while q:
                (r,c) = q.popleft()
                visited.add((r,c))
                
                for (dr,dc) in directions:
                    row = r + dr
                    col = c + dc
                    if row in range(rows) and col in range(cols) and grid[row][col] == "1" and (row,col) not in visited :
                        q.append((row,col))
        

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and grid[r][c]=="1":
                    bfs(r,c)
                    count+=1

        return count