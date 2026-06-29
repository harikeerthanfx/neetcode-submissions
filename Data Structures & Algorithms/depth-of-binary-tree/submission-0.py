# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    count=0
    max=0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root==None: return 0

        self.count=self.count+1
        if self.count>self.max: self.max=self.count

        if root.left:
            self.maxDepth(root.left)
            self.count-=1

        if root.right:
            self.maxDepth(root.right)
            self.count-=1

        return self.max