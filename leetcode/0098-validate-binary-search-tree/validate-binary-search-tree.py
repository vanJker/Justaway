# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    1. DFS with recursion: $O(n)$ and $O(n)$
    With the assistance of minimum and maximum values.
    '''
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(root, minVal, maxVal):
            if not root:
                return True
            if not (minVal < root.val < maxVal):
                return False
            return (valid(root.left, minVal, root.val) and
                    valid(root.right, root.val, maxVal))
        return valid(root, float("-inf"), float("inf"))