# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. $O(n)$ and $O(1)$
    Reverse and then remove the n-th node from head, finally reverse.
    2. $O(n)$ and $O(1)$
    Using two pointers to identify node which should be removed.
    ```
    1 -> 2 -> 3 -> 4 -> 5 -> None
                   ^---------^
    1 -> 2 -> 3 -> 4 -> 5 -> None
    ^---------^
    ```
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode()
        dummy.next = head
        left, right = dummy, head
        while n > 0 and right:
            right = right.next
            n -= 1
        while right:
            left, right = left.next, right.next
        left.next = left.next.next
        return dummy.next