# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. $O(n)$ and $O(1)$
    Using slow and fast pointers to split list into two parts: left and right.
    Then reverse right part. Finally merge left and right parts node by node.
    ```
    Original:  1 -> 2 -> 3 -> 4
    Split:     1 -> 2    3 -> 4
    Reverse:   1 -> 2    4 -> 3
    Merge:     1 -> 4 -> 2 -> 3
    ```
    '''
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        left, right = head, slow.next
        slow.next = None

        prev, curr = None, right
        while curr != None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        right = prev

        while left and right:
            nextLeft, nextRight = left.next, right.next
            left.next = right
            right.next = nextLeft
            left, right = nextLeft, nextRight