# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def lowestCommonAncestor(self, root, p, q):

        lca = root

        def search(node):

            nonlocal lca

            # CASE 1:
            # Both p and q are smaller than current node.
            # So LCA must exist in LEFT subtree.
            if p.val < node.val and q.val < node.val:
                lca = node
                return search(node.left)

            # CASE 2:
            # Both p and q are greater than current node.
            # So LCA must exist in RIGHT subtree.
            if p.val > node.val and q.val > node.val:
                lca = node
                return search(node.right)

            # CASE 3:
            # One node IS the current node,
            # and the other node is somewhere above/below it.
            #
            # Example:
            # current = 5
            # p = 5
            # q = 8
            #
            # Then current node itself becomes LCA.
            if (
                (p.val == node.val and q.val != node.val)
                or
                (q.val == node.val and p.val != node.val)
            ):
                lca = node
                return

            # CASE 4:
            # One node lies on LEFT side
            # and the other lies on RIGHT side.
            #
            # Example:
            # p = 2
            # q = 8
            # current = 5
            #
            # Then current node is the split point,
            # hence it becomes the LCA.
            if (
                (p.val < node.val and q.val > node.val)
                or
                (p.val > node.val and q.val < node.val)
            ):
                lca = node
                return

        search(root)

        return lca