class Solution:
    '''
    1. Brute force: $O(n^2)$ and $O(1)$
    2. hashing: $O(n)$ and $O(n)$
    3. Floyd algorithm: $O(n)$ and $O(1)$
    Treat index as the linked list node's next pointer.
    '''
    def findDuplicate(self, nums: List[int]) -> int:
        # detect cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # find the fork
        fast = 0
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow
