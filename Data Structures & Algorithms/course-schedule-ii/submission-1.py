class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        
        visited = set()
        order = []

        def dfs(i):
            if preMap[i] == []:
                if i not in order:
                    order.append(i)
                return True
            
            if i in visited:
                return False
            
            visited.add(i)
            for nei in preMap[i]:
                if not dfs(nei):
                    return False
            visited.remove(i)
            order.append(i)
            preMap[i] = []
            return True
            
        
        for i in range(numCourses):
            if not dfs(i):
                return []
        
        return order

