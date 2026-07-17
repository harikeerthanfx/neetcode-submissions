# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        self.condition = 1;

        def height(node):
            if not node:
                return -1;
            left_ht = height(node.left);
            right_ht = height(node.right);
            return 1 + max(left_ht,right_ht);

        def dfs_balanced(root):
            if not root:
                return;
            dfs_balanced(root.left);
            dfs_balanced(root.right);
            if abs(height(root.left)-height(root.right))>1:
                self.condition = 0;
            
        dfs_balanced(root);
        if self.condition == 0:
            return False;
        else:
            return True;

            
        

