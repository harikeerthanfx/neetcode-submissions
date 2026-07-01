class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows,cols = len(grid),len(grid[0])
        
        def bfs(a,b):
            q = collections.deque()
            q.append((a,b))
            drs = [(0,1),(1,0),(0,-1),(-1,0)]

            while q:
                (r,c) = q.popleft()
                visited.add((r,c))

                for dr,dc in drs:
                    new_r = r+dr
                    new_c = c+dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == "1" and (new_r,new_c) not in visited:
                        q.append((new_r,new_c))

                
        count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        
        return count