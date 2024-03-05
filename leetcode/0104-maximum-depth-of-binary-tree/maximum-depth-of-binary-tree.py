# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from inspect import stack
from platform import node


class Solution:
    '''
    1. DFS: $O(n)$ and $O(n)$
    2. BFS: $O(n)$ and $O(n)$
    3. Interative DFS: $O(n)$ and $O(n)$
    '''

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        level = 0
        q = deque()
        q.append(root)
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            level += 1
        return level

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        res = 0
        stack = [[root, 0]]
        while stack:
            node, depth = stack.pop()
            if node.right:
                stack.append([node.right, depth + 1])
            if node.left:
                stack.append([node.left, depth + 1])
            res = max(res, depth + 1)
        return res