class Solution:
    '''
    1. Brute force: $O(n^2)$ and $O(1)$
    2. Two pointers: $O(n)$ and $O(1)$
    '''
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        while left < right:
            current = numbers[left] + numbers[right]
            if current < target:
                left += 1
            elif current > target:
                right -= 1
            else:
                return [left + 1, right + 1]
        return []