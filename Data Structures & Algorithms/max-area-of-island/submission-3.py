class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visited = set()
        rows,cols = len(grid),len(grid[0])
        max_area = 0
        
        def bfs(a,b):
            q = collections.deque()
            q.append((a,b))
            drs = [(0,1),(1,0),(0,-1),(-1,0)]
            area = 0

            while q:
                (r,c) = q.popleft()
                visited.add((r,c))
                area += 1

                for dr,dc in drs:
                    new_r = r+dr
                    new_c = c+dc
                    if new_r in range(rows) and new_c in range(cols) and grid[new_r][new_c] == 1 and (new_r,new_c) not in visited:
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
            return area

                
        area = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    area = max(area,bfs(r,c))
        
        return area