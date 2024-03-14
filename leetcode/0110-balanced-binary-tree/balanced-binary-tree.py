# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    Recursion: $O(n)$ and $O(n)$
    Length of a path is represented by the number of nodes, the height of a None node is 0.
    And balances of subtrees are only retained one, unlike height which must be remained.
    '''
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root):
            if not root:
                return (0, True)
            lh, lb = dfs(root.left)
            rh, rb = dfs(root.right)
            return (max(lh, rh) + 1, lb and rb and abs(lh - rh) <= 1)
        _, balance = dfs(root)
        return balance

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balance = True
        def dfs(root):
            nonlocal balance
            if not balance or not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            balance = balance and abs(left - right) <= 1
            return max(left, right) + 1
        dfs(root)
        return balance