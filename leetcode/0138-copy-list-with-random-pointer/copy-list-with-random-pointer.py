"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    '''
    1. Two passes: $O(n)$ and $O(n)$
    1st pass: deep copy list and create a hashmap between old node and new node
    2nd pass: using hashmap to set new nodes' next and random
    '''
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        oldToCopy = {}
        curr = head
        while curr:
            copy = ListNode(curr.val)
            oldToCopy[curr] = copy
            curr = curr.next
        curr = head
        while curr:
            copy = oldToCopy[curr]
            copy.next = oldToCopy.get(curr.next, None)
            copy.random = oldToCopy.get(curr.random, None)
            curr = curr.next
        return oldToCopy[head]
