class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) < 2:
            return True

        adjlist = []

        for _ in range(numCourses):
            adjlist.append([])
        
        for a,b in prerequisites:
            adjlist[a].append(b)
        
        inPath = set()
        def dfs(node):
            if node in inPath:
                return False  # cycle!
            if node in visited:
                return True  # already confirmed safe, no need to recheck

            inPath.add(node)

            for neighbor in adjlist[node]:
                if not dfs(neighbor):
                    return False

            inPath.remove(node)   # <-- leaving this node, it's no longer "in progress"
            visited.add(node)     # <-- and now it's permanently safe
            return True
        
        #print(adjlist)
        visited = set()
        for i in range(numCourses):
            if i not in visited:
                if not dfs(i):
                    return False

        return True

