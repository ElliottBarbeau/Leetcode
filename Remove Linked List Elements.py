# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        prev, current = None, head
        while current and current.next:
            if current.val == val:
                prev.next = current.next
            else:
                prev = current
                
            current = current.next
            
        if current.next.val == val:
            current.next = None

        return head