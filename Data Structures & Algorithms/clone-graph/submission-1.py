"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None

        visited = set()
        queue = collections.deque()
        queue.append(node)
        exist = {}

        while queue:
            temp = queue.popleft()
            if temp not in visited:
                if temp.val not in exist:
                    node1 = Node(temp.val)
                    exist[temp.val] = node1
                node1 = exist[temp.val]
                visited.add(temp)
                for nb in temp.neighbors:
                    if nb.val not in exist:
                        new_nb = Node(nb.val)
                        exist[nb.val] = new_nb
                    new_nb = exist[nb.val]
                    node1.neighbors.append(new_nb)
                    queue.append(nb)
        res = exist[node.val]
        return res
        