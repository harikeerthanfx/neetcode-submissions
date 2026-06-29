# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: #(0,0 done here)
            return True
        if not p or not q: #(only checks 1,0 and 0,1....0,0 wont even enter into the if stmt)
            return False
        return (p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right))
        
