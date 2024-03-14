# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    1. Brute force merge: $O(n \times k)$ and $O(1)$
    2. Mergesort: $O(m \times logk)$ and $O(1)$
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        n, cnt = 1, len(lists)
        while cnt > 1:
            for i in range(0, len(lists), 2 * n):
                p = lists[i]
                q = lists[i + n] if i + n < len(lists) else None
                lists[i] = self.mergeTwoLists(p, q);
            n, cnt = n * 2, cnt // 2 if cnt % 2 == 0 else cnt // 2 + 1
        return lists[0]
        
    def mergeTwoLists(self, p: Optional[ListNode], q: Optional[ListNode]) -> Optional[ListNode]:
        if not q:
            return p
        if not p:
            return q
        dummy = ListNode()
        tail = dummy
        while p and q:
            if p.val <= q.val:
                tail.next = p
                p = p.next
            else:
                tail.next = q
                q = q.next
            tail = tail.next 
        if p:
            tail.next = p
        if q:
            tail.next = q
        return dummy.next