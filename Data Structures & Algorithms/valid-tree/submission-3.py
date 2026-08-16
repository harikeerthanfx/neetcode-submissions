class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        adjList = {i:[] for i in range(n)}
        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        visit = set()

        #only checks mainly for cycle
        def dfs(i,prev):
            if i in visit:
                return False

            visit.add(i)
            for nei in adjList[i]:
                if nei == prev:
                    continue
                if not dfs(nei,i):
                    return False
            return True
        
        return dfs(0,-1) and len(visit)==n



        
