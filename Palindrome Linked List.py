# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        slow, fast = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        last = self.reverse(slow)
        
        while head and last:
            if head.val != last.val:
                return False
            head = head.next
            last = last.next
            
        return True
            
        
    def reverse(self, node):
        prev, next = None, None
        while node:
            next = node.next
            node.next = prev
            prev = node
            node = next
            
        return prev