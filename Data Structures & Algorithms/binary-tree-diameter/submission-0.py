# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def node_ht(self,root:Optional[TreeNode])->int:
        if root==None:return 0

        left_ht=self.node_ht(root.left)
        right_ht=self.node_ht(root.right)

        return 1+max(left_ht,right_ht)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root==None : return 0

        queue=deque([root])

        diameter=0
        while(queue):
            node=queue.pop()
            d = self.node_ht(node.left)+self.node_ht(node.right)
            if d>diameter: diameter=d

            if node.left: queue.append(node.left)
            if node.right: queue.append(node.right)

        return diameter
