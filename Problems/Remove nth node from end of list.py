# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1, head)
        first, second = dummy, dummy
        
        for _ in range(n):
            second = second.next
        
        while second.next:
            first = first.next
            second = second.next
            
        first.next = first.next.next
        return dummy.next