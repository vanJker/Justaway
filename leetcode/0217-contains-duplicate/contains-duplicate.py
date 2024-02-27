class Solution:
    '''
    1. Brute force: $O(n^2)$ and $O(1)$
    ```
    for (i = 0; i < n; i++)
        for (j = i + 1; i < n; j++)
    ```
    2. Sort: $O(nlogn)$ and $O(1)$
    ```
    sort(nums)
    for (i = 0, j = 1; j < n; i++, j++)
    ```
    3. Hashset: $O(n)$ and $O(n)$
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in nums:
            if x in hashset:
                return True
            hashset.add(x)
        return False
        