class Solution:
    '''
    1. Brute force: $O(n^2)$ and $O(1)$
    2. Two pointers: $O(n)$ and $O(1)$
    '''
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l, r = 0, len(height) - 1
        while l < r:
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res