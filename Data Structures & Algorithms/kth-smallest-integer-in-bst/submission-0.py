# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0

        def ino(node):
            if not node:
                return None
            
            #travel left
            left = ino(node.left)

            if left is not None:
                return left
            
            #visit current node
            self.count += 1
            if self.count == k:
                return node.val
            
            #search right
            return ino(node.right)
            
        return ino(root)
        
            
        