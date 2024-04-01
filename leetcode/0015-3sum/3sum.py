class Solution:
    '''
    1. Brute force: $O(n^3)$ and $O(1)$ 
    triple for loop
    2. Sort and hashing: $O(n^2)$ and $O(n)$
    Firstly sort the array, then using hashing to solve the 2 sum problem.
    3. Sort and hashing: $O(n^2)$ and $O(1)$
    Firstly sort the array, then using two pointers to solve the 2 sum problem.
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, x in enumerate(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = x + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([x, nums[l], nums[r]])
                    l, r = l + 1, r - 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res