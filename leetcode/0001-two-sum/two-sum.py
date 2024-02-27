class Solution:
    '''
    1. Brute force: $O(n^2)$ and $O(1)$
    ```
    for (i = 0; i < n; i++)
        for (j = i + 1; j < n; j++)
    ```
    2. HashMap of value and index: $O(n)$ and $O(n)$
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} # value : index
        for i, x in enumerate(nums):
            diff = target - x
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[x] = i