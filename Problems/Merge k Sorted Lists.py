# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
from heapq import heappush, heappop
class Solution:
    def mergeKLists(self, lists) -> ListNode:
        minheap = []
        for l in lists:
            while l:
                heappush(minheap, l.val)
                l = l.next
                
        dummy = curr = ListNode(-1)
        while minheap:
            v = heappop(minheap)
            curr.next = ListNode(v)
            curr = curr.next
            
        return dummy.next