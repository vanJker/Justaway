# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    $O(n)$ and $O(1)$
    Similat to full-adder, using a temporary variable to store the carry. Consider carefully about the last carry!
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail, carry = dummy, 0
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            val = val1 + val2 + carry
            carry = val // 10
            tail.next = ListNode(val % 10)
            tail = tail.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next