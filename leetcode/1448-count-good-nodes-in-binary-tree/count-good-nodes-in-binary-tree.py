# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    a. Recursion DFS: $O(n)$ and $O(n)$
    '''
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, floorVal):
            if not root:
                return 0
            res = 1 if root.val >= floorVal else 0
            floorVal = max(root.val, floorVal)
            res += dfs(root.left, floorVal)
            res += dfs(root.right, floorVal)
            return res
        return dfs(root, root.val)