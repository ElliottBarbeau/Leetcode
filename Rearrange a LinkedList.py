from __future__ import print_function


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()


def reorder(head):
    count = 0
    counter = head
    while counter:
        count += 1
        counter = counter.next

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    end = reverse(slow)
    start = head

    while start and end:
        next = start.next
        start.next = end
        start = next
        end_next = end.next
        end.next = start
        end = end_next

    return head

def reverse(head):
    prev = None
    while head:
        next = head.next
        head.next = prev
        prev = head
        head = next

    return prev

def main():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    head.next.next.next.next.next.next = Node(14)
    reorder(head)
    head.print_list()


main()
