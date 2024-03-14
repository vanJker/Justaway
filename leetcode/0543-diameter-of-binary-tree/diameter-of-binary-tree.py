# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion: $O(n)$ and $O(n)$.
    Since length of a path is represented by the number of edges, the height of a None node is -1.
    And diamaters of subtrees are only retained one, unlike height which must be remained.
    '''
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if not root:
                return (-1, -1)
            lh, ld = dfs(root.left)
            rh, rd = dfs(root.right)
            return (max(lh, rh) + 1, max(ld, rd, lh + rh + 2))
        _, diameter = dfs(root)
        return diameter
        
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root):
            nonlocal res
            if not root:
                return -1
            left = dfs(root.left)
            right = dfs(root.right)
            res = max(res, left + right + 2)
            return max(left, right) + 1
        dfs(root)
        return res