# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from heapq import *
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        minheap = []
        curr = head
        while curr:
            heappush(minheap, curr.val)
            curr = curr.next
            
        dummy = ListNode(-1, head)
        while minheap and head:
            head.val = heappop(minheap)
            head = head.next
        
        return dummy.next