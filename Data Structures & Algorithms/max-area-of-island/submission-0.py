class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        visited = set()
        self.max_area = 0
        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            queue = collections.deque()
            queue.append((r,c))
            directions = [(0,1),(1,0),(-1,0),(0,-1)]
            area = 1
            visited.add((r,c))
            
            while queue:
                (R,C) = queue.popleft()

                for (dr,dc) in directions:
                    nr, nc = R + dr, C + dc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        queue.append((nr,nc))
                        visited.add((nr,nc))
                        area += 1
            
            if area > self.max_area:
                self.max_area = area
                    

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    bfs(r,c)
        
        return self.max_area