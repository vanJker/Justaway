# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. Two pointers: $O(n)$ and $O(1)$
    2. Recursion: $O(n)$ and $O(n)$
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head
        while curr != None:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        newhead = self.reverseList(head)
        head.next.next = head
        head.next = None
        return newhead