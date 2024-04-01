# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. DFS with recursion: $O(n)$ and $O(n)$
    1. DFS with iteration: $O(n)$ and $O(n)$
    '''
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = 0
        def dfs(root):
            nonlocal k
            nonlocal res
            if not root:
                return;
            dfs(root.left)
            k -= 1
            if k == 0:
                res = root.val
            dfs(root.right)
        dfs(root)
        return res

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = [root]
        cur = root.left
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            k -= 1
            if k == 0:
                return cur.val
            cur = cur.right
